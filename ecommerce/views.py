from django.shortcuts import render, HttpResponse
# from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1 style=color:teal;>My first webpage with python Django</h1>")
