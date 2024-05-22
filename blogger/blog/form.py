from typing import Any
from django import forms
from .models import Profile, Blog, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}))
    class Meta:
        model = User
        fields = ['username', 'email' , 'password1', "password2"]

    def __init__(self, *args: Any, **kwargs: Any):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['username'].label = ''
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Username'
        self.fields['username'].help_text = '<span class="form-text">Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</span>'


        self.fields['password1'].label = ''
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'

        self.fields['password2'].label = ''
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Conform Password'


class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField(label='', required=False ,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Email'}))
    first_name = forms.CharField(label='', required=False ,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'First Name', 'aria-label' : 'First Name'}))
    last_name = forms.CharField(label='', required=False ,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Last Name', 'aria-label' : 'Last Name'}))
    username = forms.CharField(label='', required=False ,widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Username', }))
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


class ProfilePicForm(forms.ModelForm):
    profile_pic = forms.ImageField(label='', widget=forms.FileInput(attrs={'class' : 'form-control', 'id' : 'image'}))
    class Meta:
        model = Profile
        fields = ['profile_pic']

class Add_blog(forms.ModelForm):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class' : 'form-control',"id" : 'title', 'placeholder' : 'Post Title'}), required=True)
    thumbnail_image = forms.ImageField(label='', widget=forms.FileInput(attrs={'class' : 'form-control', 'id' : 'image'}))
    body = forms.CharField(widget=CKEditorWidget(), required=True)
    class Meta:
        model = Blog
        fields = ['title',"category", 'thumbnail_image', 'body']
        labels = {'category': '', 'body' : ''}
        # exclude = ['user',]
        widgets = {'category': forms.Select(attrs={'class': 'form-select', "id" : 'select_category'}),}
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        # exclude = ['user',]
        labels = {'name' : ''}
        widgets = {'name' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Add Category'})}