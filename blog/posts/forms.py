from django import forms
from django.forms import ModelForm
from categories.models import Categories
from .models import Posts

class PostsForm(ModelForm):
    category = forms.ModelChoiceField(label='Category', empty_label='Null' , queryset=Categories.objects.all(), required=False)
    class Meta:
        model = Posts
        fields = ['title', 'description', 'image', 'category']
        

