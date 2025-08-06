from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [

    path("",views.homepage,name='home'),
    path("booking/",views.booking, name='book'),
    path('bike/<int:bike_id>/', views.bike_detail, name='bike_detail'),
]



