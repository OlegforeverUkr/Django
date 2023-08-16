from django import forms
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': "form-control form-control-xs", 
            'name': 'username',
            'placeholser': 'Username'
        }
    ))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': "form-control form-control-xs", 
            'name': 'password',
            'placeholser': 'Password'
             }))

    def clean(self):
        if authenticate(**self.cleaned_data) is None:
            raise ValidationError('Incorrect username or password')


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={
            'class': "form-control form-control-xs", 
            'name': 'username',
            'placeholser': 'Username'
        }
    ))

    email = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={
            'class': "form-control form-control-xs", 
            'name': 'email',
            'placeholser': 'Email'
        }
    ))

    password = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={
            'class': "form-control form-control-xs", 
            'name': 'password',
            'placeholser': 'Password'
             }))

    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={
            'class': "form-control form-control-xs", 
            'name': 'confirm_password',
            'placeholser': 'Confirm Password'
             }))

    def create_user(self):
        del self.cleaned_data['confirm_password']
        UserModel.objects.create_user(**self.cleaned_data)


    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            if UserModel.objects.get(username=username):
                raise ValidationError('User with the same username already exists')
        except UserModel.DoesNotExist:
            return username


    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
            self.add_error('password', 'Does not match')
            self.add_error('confirm_password', 'Does not match')