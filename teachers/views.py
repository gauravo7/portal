from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome to First URL of the Page from View.py");
def about(request):
    return HttpResponse("You are in the ABout Section")
def contact(request):
    return HttpResponse("You are seeing Contact Page")