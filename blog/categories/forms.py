from django.forms import ModelForm
from .models import Categories

class CategoryForm(ModelForm):
    class Meta:
        model = Categories
        fields = ['title']