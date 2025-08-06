from django.contrib import admin
from django.urls import path
from .import views
from django.http import HttpResponse

urlpatterns = [

    path("",views.homepage,name='home'),
    path("booking/",views.booking, name='book'),
    path('bike/<int:bike_id>/', views.bike_detail, name='bike_detail'),
    path('favicon.ico', lambda request: HttpResponse(status=204)),

]



