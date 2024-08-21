from django import forms
from django.contrib.auth.models import User
from .models import Blog

class BlogForm(forms.ModelForm):
    author = forms.ModelChoiceField(
        queryset=User.objects.all(),  
        empty_label='Select an author'
    )
    
    class Meta:
        model = Blog
        fields = ['author', 'title', 'content', 'is_published']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['author'].queryset = User.objects.all()
        
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
