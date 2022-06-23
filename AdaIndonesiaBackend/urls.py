from django.contrib import admin
from django.urls import path

from mainapp import views as mainApp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/post/data/get/all', mainApp.getDataPostAll),
    path('api/post/<str:slug>', mainApp.detailPost)
]
