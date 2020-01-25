"""Users app forms"""

from django import forms

from django.contrib.auth.models import User


class UserForm(forms.Form):
    """User form"""
    username = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput)
    password_confirmation = forms.CharField(max_length=128, widget=forms.PasswordInput)

    def clean_email(self):
        """Validates if email is unique"""
        email = self.cleaned_data.get('email')
        user_exists = User.objects.filter(email=email).exists()
        if user_exists:
            raise forms.ValidationError('Este correo ya está en uso')
        return email

    def clean(self):
        """Validates if passwords do match"""
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        if not password or password != password_confirmation:
            raise forms.ValidationError('Las contraseñas no coinciden.')

        return self.cleaned_data

    def save(self):
        """Saves user"""
        data = self.cleaned_data
        data.pop('password_confirmation')

        return User.objects.create_user(**data)
