from django.contrib import admin
from .models import Bike, Specfication
# Register your models here.



class SpecInline(admin.StackedInline):
    model = Specfication
    extra = 0

class BikeAdmin(admin.ModelAdmin):
    model = Bike
    inlines = [SpecInline]

admin.site.register(Bike,BikeAdmin)