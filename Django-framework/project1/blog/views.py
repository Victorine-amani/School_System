from django.shortcuts import render

from django.http import HttpResponse, request

#when a user wants to go to the home page
def home(request):
    return HttpResponse('<h1 style="color:green; text-align:center">Blog Home</h1><h3 style="color:orange;text-align:center">I am learning django by creating a web blog<h3>')



def about(request):
    return HttpResponse('<h1>Blog About</h1>')