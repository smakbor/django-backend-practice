from django.shortcuts import render,HttpResponse

# Create your views here.
def inventory(request):
    return render(request,"inventory/inventory.html")
