from django import forms
from post.models import Company, Post


class CreateCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter blogs title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something down here...'}),
        }


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter post title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write something down here...'}),
        }

