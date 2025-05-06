from django import forms
from .models import Blog, Tag

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class BlogForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'id_tags'}),
        required=False
    )

    class Meta:
        model = Blog
        fields = ['title', 'content', 'image', 'tags']