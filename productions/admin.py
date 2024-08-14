from django.contrib import admin
from .models import Prod, Comment


@admin.register(Prod)
class Adminproductuion(admin.ModelAdmin):
    list_display = ['title', 'price', 'status', ]

# admin.site.register(Customizeuser, Customadmin)


@admin.register(Comment)
class Adminproductuion(admin.ModelAdmin):
    list_display = ['prodd', 'author', 'body', 'stars', 'active', ]
