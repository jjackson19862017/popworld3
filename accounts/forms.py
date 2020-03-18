from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import UserProfile


class UserLoginForm(forms.Form):
    """
    Form to be used to log users in
    """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    Form to Create the User
    """

    first_name = forms.CharField(label="Forename")
    last_name = forms.CharField(label="Surname")

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username',  'password1', 'password2','email','first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        forename = self.cleaned_data.get('forename')
        surname = self.cleaned_data.get('surname')

        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['telephone','address1','town','county','postcode','country']