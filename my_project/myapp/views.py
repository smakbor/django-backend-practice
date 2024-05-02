from django.shortcuts import render,HttpResponse

# Create your views here.

def Student(request):
    return HttpResponse("Hello world. This is root Url and student function")
 
def PrintName(request):
    return HttpResponse("Hey my name is Akbor")