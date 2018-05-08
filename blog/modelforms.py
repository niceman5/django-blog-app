from django.forms import forms
from .models import Post


class PostModelForm(forms.ModelForm):
    class Meta:
        mode = Post
        fields = ['title','text',]