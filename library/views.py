from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Book, Log
import json
#needed for fixing flaws, but kept here for simplicity:
import time #FLAW 3: returnTime
from django.views.decorators.csrf import csrf_protect #FLAW 1: CSRF

# Create your views here.

def index(request):
    allBooks = Book.objects.all() #get all books from the database
    #currentTime = time.time()//1  #FLAWS 3&4: returnTime and timestamp
    #FLAW 3: if a book has been borrowed for too long: return it automatically
    #FLAW 3, uncomment the next six lines
    #for book in allBooks:
    #    if book.borrowed == 1 and book.returnTime < currentTime:
    #        book.borrowed = 0 #return the book
    #        book.returnID = "" #remove the returnID
    #        book.returnTime = 0 #remove the returnTime
    #        book.save() #store the information
    availableBooks = Book.objects.filter(borrowed = 0) #get all books that are not yet borrowed
    #FLAW 4: uncomment the next four lines for logging
    #log_time = currentTime #timestamp for the log
    #log_request = str(request) #the request in text format
    #log_available = len(availableBooks) #number of available books in the system
    #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "OK") #save the log
    return render(request, "pages/index.html", context = {'books' : allBooks, 'available' : availableBooks})

#@csrf_protect #FLAW 1: CSRF
def readbook(request, title):
    #currentTime = time.time()//1 #FLAWS 3&4, current time and timestamp
    #FLAW 4, uncomment the next four lines for logging
    #log_time = currentTime #timestamp for log
    #log_request = str(request) #request in text format
    #availableBooks = Book.objects.filter(borrowed = 0) #get all books that are not yet borrowed
    #log_available = len(availableBooks) #number of available books
    #if request.method != "POST": #FLAW 1, method should be POST for CSRF; uncomment this line, but not the next
        #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "NOT_POST_METHOD") #FLAW 4: log
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to incorrectly access a book."}) #FLAW 1
    #else the method = POST:
    try:
        book = Book.objects.get(title = title) #get the book with the requested title
    except: #if it does not exist in the database, return error
        #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "BOOK_DOES_NOT_EXIST") #FLAW 4: log
        return render(request, "pages/error.html", context = {'msg' : "You tried to access a non-existing book."})
    #FLAW 2: prevent borrowing of an already borrowed book
    #if book.borrowed == 1: #FLAW 2, uncomment this line, but not the next, yet
        #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "ALREADY_BORROWED") #FLAW 4: log
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to access an already borrowed book."}) #FLAW 2
    #book.returnID = request.COOKIES['csrftoken'] #FLAW 2: prevent returning of someone else's book
    #book.returnTime = currentTime + 20 #FLAW 3: returnTime is set to 20 secs after borrowing, to allow automatic return
    book.borrowed = 1 #register book as borrowed
    book.save() #store information about book
    #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "OK") #FLAW 4: log
    return render(request, "pages/readbook.html", context = {'book' : book})

#@csrf_protect #FLAW 1: CSRF
def returnBook(request, title): #FLAW 2, replace this line with the next
#def returnBook(request, title, returnID): #FLAW 2, replace above line with this
    #FLAW 4, uncomment the next four lines for logging
    #log_time = time.time()//1 #timestamp
    #log_request = str(request) #request in text format
    #availableBooks = Book.objects.filter(borrowed = 0) #get all books that are not yet borrowed
    #log_available = len(availableBooks) #number of available books
    #if request.method != "POST": #FLAW 1, method should be POST for CSRF; uncomment this line, but not the next, yet
        #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "NOT_POST_METHOD") #FLAW 4: log
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to incorrectly access a book."}) #FLAW 1
    #else the method = POST:
    try:
        book = Book.objects.get(title = title) #get the book with the requested title
    except: #if it does not exist in the database, return error
        #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "BOOK_DOES_NOT_EXIST") #FLAW 4: log
        return render(request, "pages/error.html", context = {'msg' : "You tried to access a non-existing book."})
    #FLAW 2: prevent returning of someone else's book
    #if book.returnID != returnID:  #FLAW 2, uncomment this line but not the next, yet
        #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "WRONG_RETURN_ID") #FLAW 4: log
    #    return render(request, "pages/error.html", context = {'msg' : "You tried to return a book incorrectly."}) #FLAW 2
    book.borrowed = 0 #register book as returned
    book.save() #store book information
    #Log.objects.create(timestamp = log_time, request = log_request, available = log_available, status = "OK") #FLAW 4
    return redirect("/library")
