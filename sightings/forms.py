from django import forms
from django.forms import fields
from django.forms import widgets
from .models import Squirrel
from django.forms import ModelForm


class SquForm(ModelForm):
    class Meta:
        model=Squirrel
        fields='__all__'
