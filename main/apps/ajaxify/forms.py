from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title    = forms.CharField(widget=forms.TextInput(), max_length=120)
    message  = forms.CharField(widget=forms.Textarea(), max_length=255)

    class Meta:
        model = Post
        fields = ['title', 'message']
