from django.contrib import admin
from django.urls import path
from todo_list import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
]
