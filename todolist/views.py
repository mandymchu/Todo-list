from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

def index(request):
	message = "Current time: {}".format(datetime.datetime.now())
	return HttpResponse(message)