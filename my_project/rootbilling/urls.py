from django.urls import path
from . import views


urlpatterns = [
    path("rootbilling/",views.rootbilling,name="data"),
  
]
