from django.shortcuts import render,HttpResponse

# Create your views here.
def newsPaper(request):
    return HttpResponse("This is news paper function")