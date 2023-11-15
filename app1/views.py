from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def fun1(request):
    return HttpResponse('<h1>specific url for app1_fun1</h1>')
def fun2(request):
    return HttpResponse('<h1>specific url for app1_fun2</h1>')