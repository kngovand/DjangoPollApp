from django.shortcuts import render
from django.http import httpResponse

def index(request):
    return httpResponse("hi there. you are in polls index.")