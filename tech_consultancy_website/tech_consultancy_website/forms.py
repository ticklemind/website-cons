from django import forms
from .models import BlogPost

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class TestimonialForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)
    author = forms.CharField(max_length=100)

class AppointmentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=20)
    date = forms.DateTimeField()
    message = forms.CharField(widget=forms.Textarea)

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'author']

