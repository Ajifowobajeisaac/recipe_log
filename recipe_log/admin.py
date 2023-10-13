from django.contrib import admin

# Register your models here.

from .models import Recipe_name, Entry

admin.site.register(Recipe_name)
admin.site.register(Entry)
