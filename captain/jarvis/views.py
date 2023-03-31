from django.shortcuts import render
from django.http import HttpResponse

def ultron(request):
    return HttpResponse('<h1>   POWERSTAR  </h1>')


def janasena(request):
    return HttpResponse('<marquee><h1>MANALNI EVADU RA APEDHI</h1></marquee>')