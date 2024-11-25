from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse

def shopping(request):
    return HttpResponse('<h1> Happy Shopping </h1>')
