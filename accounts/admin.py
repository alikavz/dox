from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import Usercreation, UserChangeForm
from .models import Customizeuser


class Customadmin(UserAdmin):
    add_form = Usercreation
    form = UserChangeForm
    model = Customizeuser
    list_display = ['username', 'email', ]


admin.site.register(Customizeuser, Customadmin)
