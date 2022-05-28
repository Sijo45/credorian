from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django import template

# Create your views here.
def home(request):
       return render(request,'home.html')
def sign(request):
       return render(request,'sign.html')
