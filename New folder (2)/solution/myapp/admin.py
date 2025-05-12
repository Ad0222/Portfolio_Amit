from django.contrib import admin
from .models import MyModel
# Register your models here.

admin.site.register(MyModel)

# # myapp/admin.py

# from django.contrib import admin
# from .models import MyImage

# class MyImageAdmin(admin.ModelAdmin):
#     list_display = ['image']

# admin.site.register(MyImage)
