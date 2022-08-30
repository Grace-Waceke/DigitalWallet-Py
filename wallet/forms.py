
from django import forms
from .models import Customer
from django.forms import ModelForm

class CustomerRegistrationForm(ModelForm):
    class Meta:
        model=Customer
        fields="__all__"