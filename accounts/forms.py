from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Customizeuser
from django.contrib.auth import get_user_model


class Usercreation(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email',)  # UserCreationForm.Meta.fields + ('sen',)


class Userchange(UserChangeForm):
    class Meta:
        model = get_user_model()
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email',)
