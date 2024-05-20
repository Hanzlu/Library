from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('readbook/<str:title>', views.readbook, name='readbook'),
    path('return/<str:title>', views.returnBook, name='return') #remove and replace with the below for FLAW 2
    #path('return/<str:title>/<str:returnID>', views.returnBook, name='return') #FLAW 2, add return ID to the link
]
