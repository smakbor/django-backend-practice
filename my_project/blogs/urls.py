

from django.urls import path
from . import views


urlpatterns = [
    path("create/",views.createBlog),
    path("update/",views.updateBlog),
    path("delete/",views.deleteBlogs),
]
