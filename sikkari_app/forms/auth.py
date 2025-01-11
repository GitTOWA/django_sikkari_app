# forms.py
from django import forms

class LoginForm(forms.Form):
    employee_code = forms.CharField(
        label='従業員番号',
        max_length=5,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password = forms.CharField(
        label='パスワード',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )