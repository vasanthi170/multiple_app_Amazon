from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore

def movies(request):
    return HttpResponse('Movies will be dispalyed here')