from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Book, Log
import json
#Needed for fixing flaws later:
import random, time
csrf_tokens = []
# Create your views here.

def index(request):
#   log_time = time.time()//1  #F4
#   log_requests = str(request)
#   log_borrowed = 0
#   log_tokens = len(csrf_tokens)
    #csrf_tokens.append(request.COOKIES['csrftoken']) #F5
    allBooks = Book.objects.all()
    #t = time.time() //1  #F2
    #for book in allBooks:
        #if book.borrowed = 1:  #F4
            #log_borrowed += 1
    #    if book.returnTime != 0 and book.returnTime < t:
    #        book.borrowed = 0
    #        book.returnTime = 0
    #        book.save()
    availableBooks = Book.objects.filter(borrowed = 0)
    #Log.objects.create(timestamp = log_time, request = log_requests, borrowed = log_borrowed, tokens = log_tokens) #F4
    return render(request, "pages/index.html", context = {'books' : allBooks, 'available' : availableBooks})

def readbook(request, title):
#   log_time = time.time()//1  #F4
#   log_requests = str(request)
#   log_borrowed = -1
#   log_tokens = len(csrf_tokens)
    #token = request.COOKIES['csrftoken']  #F5
    #if token in csrf_tokens:
    #    csrf_tokens.remove(token)
    #else:
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to incorrectly access a book."})
    book = Book.objects.get(title = title)
    #if book.borrowed == 1:  #F1.1
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to access an already borrowed book."})
    #book.returnID = str(random.random()) #F1.2
    book.borrowed = 1
    #book.returnTime = time.time()//1 + 20 #20 secs until returnTime #F2
    book.save()
    #Log.objects.create(timestamp = log_time, request = log_requests, borrowed = log_borrowed, tokens = log_tokens) #F4
    return render(request, "pages/readbook.html", context = {'book' : book})

def returnBook(request, title):
#def returnBook(request, title, returnID): #F1.2 replace above line with this
#   log_time = time.time()//1  #F4
#   log_requests = str(request)
#   log_borrowed = -2
#   log_tokens = len(csrf_tokens)
    book = Book.objects.get(title = title)
    #if book.returnID != returnID:  #F1.2
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to return a borrowed book incorrectly."})
    book.borrowed = 0
    book.save()
    #Log.objects.create(timestamp = log_time, request = log_requests, borrowed = log_borrowed, tokens = log_tokens) #F4
    return redirect("/library")
