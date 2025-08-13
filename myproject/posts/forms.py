from django import forms
from . import models

class CreatePost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['title', 'body', 'slug', 'banner']

class EditPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['body', 'slug', 'banner']