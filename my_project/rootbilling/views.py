from django.shortcuts import render,HttpResponse

# Create your views here.
def rootbilling(request):
    return render(request,"rootbilling/rootbilling.html")