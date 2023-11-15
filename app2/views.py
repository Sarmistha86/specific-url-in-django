from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fun1(request):
    return HttpResponse('<h1>specific url for app2_fun1</h1>')
def fun2(requert):
    return HttpResponse('<h1>specific url for app2_fun2</h1>')
