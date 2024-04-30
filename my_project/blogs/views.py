from django.shortcuts import render,HttpResponse

# Create your views here.
def createBlog(request):
    return HttpResponse("this is blog create function")

def updateBlog(request):
    return HttpResponse('This is update blogs function')

def deleteBlogs(request):
    return HttpResponse("this is delete blog fucntion")