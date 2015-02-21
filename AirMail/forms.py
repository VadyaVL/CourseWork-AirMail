__author__ = 'Vadym'

from django.forms import ModelForm
from django import forms
import models

class MessageForms(ModelForm):

    class Meta:
        model = models.Message
        fields = ['Text']

        widgets = {'Text': forms.Textarea(attrs={'cols': 5, 'rows': 5})}