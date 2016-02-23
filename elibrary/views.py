from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserFormRegister, UserForm, BookForm
from django.http import HttpResponseRedirect, HttpResponse
from .models import UserProfile, Book
from django.utils import timezone
from itertools import chain
# Create your views here.


@login_required(login_url = '/login/')
def history(request):
	userhistory = request.user.profile.history.split(',')
	user = request.user
	return render(request,'history.html', {'history': userhistory, 'user':user})

def home(request):
	return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data = request.POST)
        users_form = UserFormRegister(data = request.POST)
        if user_form.is_valid() and users_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            userregister = users_form.save(commit=False)
            userregister.user = user
            userregister.save()
            new_user = authenticate(username=request.POST['username'], password=request.POST['password'])
            login(request, new_user)
            return redirect('/allbooks/')
    else:
        user_form = UserForm()
        users_form = UserFormRegister()
    return render(request, 'register.html',{'user_form':user_form, 'users_form':users_form},)  	

def login_library(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pswd')
        user = authenticate(username = username, password = password)
        if user :
            if user.is_active:
                login(request,user)
                return redirect('/allbooks/')
            else:
                return HttpResponse('Disabled Account')
        else:
            return HttpResponse("Invalid Login details.Are you trying to Sign up?")
    else:
        return render(request,'login.html',)

@login_required
def logout_library(request):
    logout(request)
    return redirect('/')

def allbooks(request):
    books = Book.objects.all().order_by('libID')
    return render(request, 'allbooks.html',{'books':books})

def availbooks(request):
    books = Book.objects.all().order_by('libID')
    return render(request, 'availbooks.html',{'books':books})

def issueBookPage(request, bookID):
    if request.user.is_superuser:
        book = get_object_or_404(Book, id = bookID)
        return render(request, 'issuebooks.html',{'book':book, 
                                                  'RequestSapList': book.requestedBy.split(','), 
                                                  'IssueSapList': book.issuedTo.split(',')})
    else:
        return HttpResponse('You dont have permission to view this page')    

def requestbooks(request, bookID):
    if not request.user.is_superuser:
        book = get_object_or_404(Book, id = bookID)
        user = UserProfile.objects.get(SapID = request.user.profile.SapID)
        if book and book.copies > 0:
            book.requestedBy += "," + str(request.user.profile.SapID)
            book.requests += 1
            book.save()
            user.history = "Requested " + book.bookName + " on " + str(timezone.now()) + "," + user.history
            user.save()
        return render(request, 'requestbooks.html',{'bookID':request.user,'book':book.bookName})
    else :
        return HttpResponse("You're an Admin. You don't have the permission to request books.")    

def issueToUser(request, bookID, SapID):
    if request.user.is_superuser:
        book = get_object_or_404(Book, id = bookID)
        user = UserProfile.objects.get(SapID = SapID)
        if book :
            if book.copies > 0:
                book.copies -= 1
                book.requestedBy = book.requestedBy.replace(str(SapID),"")
                book.requests -= 1
                book.issuedTo += "," + str(SapID)
                book.save()   
                user.history = "Request approved for " + book.bookName + " on " + str(timezone.now()) + "," + user.history
                user.save()
                return HttpResponseRedirect('/bookissue/'+bookID+"/",{'book':book, 
                                                                      'RequestSapList': book.requestedBy.split(','), 
                                                                      'IssueSapList': book.issuedTo.split(',')})
            return HttpResponse("All copies issued.")    
    else:
        return HttpResponse('You dont have permissionto view this page')    
     
def declineIssueToUser(request, bookID, SapID):
    if request.user.is_superuser:
        book = get_object_or_404(Book, id = bookID)
        user = UserProfile.objects.get(SapID = SapID)
        if book :
            book.requestedBy = book.requestedBy.replace(str(SapID),"")
            book.requests -= 1
            book.save()
            user.history = "Request declined for " + book.bookName  + " on " + str(timezone.now()) + "," + user.history
            user.save()   
            return HttpResponseRedirect('/bookissue/'+bookID+"/",{'book':book, 
                                                                  'RequestSapList': book.requestedBy.split(','),
                                                                  'IssueSapList': book.issuedTo.split(',')})
    else:
        return HttpResponse('You dont have permissionto view this page')

def returnBook(request, bookID, SapID):
    if request.user.is_superuser:
        book = get_object_or_404(Book, id = bookID)
        user = UserProfile.objects.get(SapID = SapID)
        if book :
            book.copies += 1
            book.issuedTo = book.issuedTo.replace(str(SapID),"")
            book.save()
            user.history = book.bookName + " Returned"  + " on " + str(timezone.now()) + "," + user.history
            user.save()
            return HttpResponseRedirect('/bookissue/'+bookID+"/",{'book':book, 
                                                                  'RequestSapList': book.requestedBy.split(','), 
                                                                  'IssueSapList': book.issuedTo.split(',')})
    else:
        return HttpResponse('You dont have permissionto view this page.')

"""def addBook(request, bookID):
    if request.user.is_superuser:
        book = Book.objects.get(id = bookID)
        book.copies += 1
        book.save() 
        books = Book.objects.all()
        return HttpResponseRedirect('/allbooks/', {'books':books})
    else:
        return HttpResponse("You dont have permission to view this page.")   """            

def addNewBook(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = BookForm(data = request.POST)
            if form.is_valid():
                book = form.save()
                book.save()
                return redirect('/allbooks/')
        else :
            form = BookForm()
        return render(request, 'addnewbook.html', {'form':form})            
    else:
        return HttpResponse("You dont have permission to view this page.") 

"""def removeCopy(request, bookID):
    if request.user.is_superuser:
        book = Book.objects.get(id = bookID)
        book.copies -= 1
        if book.copies > 0 :
        	book.save()
        else :
        	book = Book.objects.get(id = bookID).delete() 
        books = Book.objects.all()
        return HttpResponseRedirect('/allbooks/', {'books':books})
    else:
        return HttpResponse("You dont have permission to view this page.") """

def editBook(request, bookID):
    if request.user.is_superuser:
        book = Book.objects.get(id = bookID).delete()    
        return redirect('/addnewbook/')
    else:
        return HttpResponse("You don't have permission to view this page.")

def removeBook(request, bookID):
    if request.user.is_superuser:
        book = Book.objects.get(id = bookID).delete()    
        books = Book.objects.all()
        return HttpResponseRedirect('/allbooks/', {'books':books})
    else:
        return HttpResponse("You don't have permission to view this page.")  	

def searchBook(request):
    if request.method == 'POST':
        keyword = request.POST['keyword']
        result1 = Book.objects.filter(bookName__icontains = keyword)
        result2 = Book.objects.filter(libID__icontains = keyword)
        result3 = Book.objects.filter(area__icontains = keyword)
        result4 = Book.objects.filter(subject__icontains = keyword)
        result5 = Book.objects.filter(author__icontains = keyword)
        result = list( set ( chain( result2, result1, result3, result4, result5)))
        return render(request, 'searchresult.html', {'result' : result},) 
    else:
        return render(request, 'searchform.html')	

