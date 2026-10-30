import re
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data["username"]
        if not re.fullmatch(r"[A-Za-z][A-Za-z0-9_]{2,29}", username):
            raise forms.ValidationError("Use 3-30 characters. Start with a letter; use letters, numbers or underscores.")
        return username

    def clean_password(self):
        password = self.cleaned_data["password"]
        if not re.fullmatch(r"(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@#$%^&+=!]{6,20}", password):
            raise forms.ValidationError("Password must be 6-20 characters and contain letters and numbers.")
        return password
