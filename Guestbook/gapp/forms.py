from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'bookname', 'feedback']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'des', 'placeholder': 'Enter your name'}),
            'email': forms.EmailInput(attrs={'class': 'des', 'placeholder': 'Enter your Email ID'}),
            'bookname': forms.TextInput(attrs={'class': 'des', 'placeholder': 'Enter the book name', 'style': 'width: 300px;'}),
            'feedback': forms.Textarea(attrs={'class': 'textarea', 'placeholder': 'Enter the feedback about book'}),
        }
