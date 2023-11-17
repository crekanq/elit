from django import forms

from .models import Comment, Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write your notes or questions here...',
        'cols': '30',
    }))

    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'email', 'message')


class CommentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'cols': '30',
    }))

    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
