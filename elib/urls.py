"""elib URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from elibrary import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.login_library, name = "home"),
    url(r'^history/$', views.history, name = "history"),
    url(r'^login/$',views.login_library ,name = 'login'),
    url(r'^logout/$',views.logout_library ,name = 'logout'),
    url(r'^register/$',views.register , name ='new_user'),
    url(r'^allbooks/$',views.allbooks , name ='allbooks'),
    url(r'^availablebooks/$',views.availbooks , name ='availbooks'),
    url(r'^bookissue/(\d{1,4})/$', views.issueBookPage, name = 'issuebooks'),
    url(r'^bookrequest/(\d{1,4})/$', views.requestbooks, name = 'requestbooks'),
    url(r'^bookissue/(\d{1,4})/issueto/(\d{10,13})/$', views.issueToUser, name = 'issueToUser'),
    url(r'^bookissue/(\d{1,4})/decline/(\d{10,13})/$', views.declineIssueToUser, name = 'declineIssueToUser'),
    url(r'^bookissue/(\d{1,4})/returnedby/(\d{10,13})/$', views.returnBook, name = 'returnBook'),
    #url (r'^addbook/(\d{1,4})/$', views.addBook, name = "addBook"),
    url(r'^addnewbook/$', views.addNewBook, name = "addnewbook"),
    #url (r'^removeCopy/(\d{1,4})/$', views.removeCopy, name = "removeCopy"),
    url (r'^removebook/(\d{1,4})/$', views.removeBook, name = "removeBook"),
    url (r'^editbook/(\d{1,4})/$', views.editBook, name = "editBook"),
    url(r'^search/$', views.searchBook, name = "searchBook")

]

