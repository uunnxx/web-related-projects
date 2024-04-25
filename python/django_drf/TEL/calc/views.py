# from django.core.handlers.asgi import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello World')
