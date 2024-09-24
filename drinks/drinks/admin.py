from django.contrib import admin
from .models import Drink

# admin.site.register(Drink)
@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
