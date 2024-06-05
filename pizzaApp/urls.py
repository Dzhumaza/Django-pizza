# pizzaApp/urls.py
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('category/<slug:category_slug>/', views.category_list, name='category_list'),
]
