from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

#def index(request):
#    return HttpResponse("everything works fine")


def home(request):
    return render(request, 'htmlpg1.html')


def signup(request):
    return render(request, 'signup.html')