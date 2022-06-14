

from http.client import HTTPResponse
from django.shortcuts import HttpResponse

def home(requst):
    return HttpResponse("hi")