from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title    = forms.CharField(widget=forms.TextInput(), max_length=120)
    message  = forms.CharField(widget=forms.Textarea(attrs={'rows':2}), max_length=255)

    class Meta:
        model = Post
        fields = ['title', 'message']


class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    message = forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write here your message!'
    )
    source = forms.CharField(       # A hidden input for internal use
        max_length=50,              # tell from which page the user sent the message
        widget=forms.HiddenInput()
    )

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        name = cleaned_data.get('name')
        email = cleaned_data.get('email')
        message = cleaned_data.get('message')
        if not name and not email and not message:
            raise forms.ValidationError('You have to write something!')
