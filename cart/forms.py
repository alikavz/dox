from django import forms


class Addtocart(forms.Form):
    CHOICES = [(i, str(i)) for i in range(1, 40)]
    quantity = forms.TypedChoiceField(choices=CHOICES, coerce=int)
    inplace = forms.BooleanField(required=False, widget=forms.HiddenInput)

