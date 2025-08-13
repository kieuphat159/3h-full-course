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

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'}),
        }