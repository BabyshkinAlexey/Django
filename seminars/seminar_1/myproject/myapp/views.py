from django.shortcuts import render
from django.http import HttpResponse

def index(reqvest):
    return HttpResponse('Hello, world!')

def about(reqvest):
    return HttpResponse('About, us')

