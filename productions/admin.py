from django.contrib import admin
from .models import Prod, Comment
from jalali_date.admin import ModelAdminJalaliMixin


class Commentinline(admin.TabularInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 0


@admin.register(Prod)
class Adminproductuion(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'price', 'status', ]

    inlines = [
        Commentinline,
    ]
# admin.site.register(Customizeuser, Customadmin)


@admin.register(Comment)
class Admincommentation(admin.ModelAdmin):
    list_display = ['prodd', 'author', 'body', 'stars', 'active', ]
