from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['topic', 'name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter room name...',
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Enter room description...'
            })
        }


class TopicForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Topic


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'password'
    }))

    class Meta:
        model = User
        fields = ['username', 'password']


class CustomUserForm(UserCreationForm):
    class Meta:
        fields = ['username', 'full_name', 'avatar', 'bio', 'email', 'password1', 'password2']
        model = User


class MessageForm(forms.ModelForm):
    body = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your message here...'
        }))

    class Meta:
        model = Message
        fields = ['body']


class UpdateUserForm(UserChangeForm):
    class Meta:
        fields = [
            'username',
            'avatar',
            'bio',
            'email',
        ]
        model = User
