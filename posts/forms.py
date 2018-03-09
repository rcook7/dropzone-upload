from django.core.validators import FileExtensionValidator
from django import forms

class PostCreateForm(forms.Form):
    title = forms.CharField()
