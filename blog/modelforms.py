# djang.forms가 아니라 djang로 import
from django import forms
from .models import Post, Comment


#validator함수지정
def min_lengthn_3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상 입력해 주세요!")

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','text',]

class PostForm(forms.Form):
    title = forms.CharField(validators=[min_lengthn_3_validator])
    text = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text',)