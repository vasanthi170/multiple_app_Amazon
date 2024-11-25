from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore

def payment(request):
    return HttpResponse('<h1>Payments will be done here </h1>')
