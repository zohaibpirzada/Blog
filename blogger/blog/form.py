from typing import Any
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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
