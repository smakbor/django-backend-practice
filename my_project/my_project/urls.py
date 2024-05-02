"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
# from myapp import views
# from blogs.views import createBlog
# from blogs.views import updateBlog
# from blogs.views import deleteBlogs
# from inventoryapp import views as ivnt
# from newsapp import views as news
# from rootbilling import views as rootB


urlpatterns = [
    path('admin/', admin.site.urls),
    # path("",views.Student),
    # path("name/",views.PrintName),
    # path("blog/create/",createBlog),
    # path("blog/update/",updateBlog),
    # path("blog/delete/",deleteBlogs),
    # path("news/", news.newsPaper),
    # path("rootbilling/",ivnt.inventory),
    # path("rootbilling/",rootB.rootbilling),
    path("blog/",include("blogs.urls")),
    path("",include("myapp.urls")),
    path("news/",include("newsapp.urls")),
    path("root/",include("rootbilling.urls")),
    path("invent/",include("inventoryapp.urls"))
]
