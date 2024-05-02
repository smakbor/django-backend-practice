from django.shortcuts import render,HttpResponse

# Create your views here.
def newsPaper(request):
    demoNews = {"test":"This is the demo news fadfdasfd"}
    return render(request,"news/news.html",context=demoNews)