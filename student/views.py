from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Index of Student App")
def about(request):
    return HttpResponse("You are in About page of Student")
def html(request):
    return render(request,"student/index.html")
def page(request):
    return render(request,"student/sub.html")
def form(request):    
    return HttpResponse(int(request.GET['num'])+int(request.GET['num2']))
def form2(request):  
    nums = [1,2,3]
    return render(request,'student/nums.html',{"nums":nums})
