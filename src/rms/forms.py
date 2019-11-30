from django.forms import Form
from django import forms


class MemberForm(Form):
    name = forms.CharField(min_length=10, max_length=255, required=True, strip=True)
    email = forms.EmailField(required=False)
    about = forms.CharField(max_length=10000, required=False, strip=True)