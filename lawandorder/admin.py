from django.contrib import admin
from .models import Order, Orderitems
from jalali_date.admin import ModelAdminJalaliMixin


class Orderinline(admin.TabularInline):
    model = Orderitems
    fields = ['order', 'productt', 'quantity', 'price', ]
    extra = 1


@admin.register(Order)
class Adminorderation(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'date_creation', 'is_paid', ]

    inlines = [
        Orderinline,
    ]
# admin.site.register(Customizeuser, Customadmin)


@admin.register(Orderitems)
class Adminordi(admin.ModelAdmin):
    list_display = ['order', 'productt', 'quantity', 'price', ]
