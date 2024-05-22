from blog.models import Profile, Category
from django import forms

class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        # fields = ['name', 'cat_image']
        exclude = ['user',]
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Add Category', 'id' : 'cat_name'}), 
            'cat_image' : forms.FileInput(attrs={'class' : 'form-control','id' : 'cat_img'})}