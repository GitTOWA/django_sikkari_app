from django import forms
from ..models import Customer

class CustomerFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '得意先コード、得意先名で検索'})
    )

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_code', 'customer_name', 'phone_number', 
                 'postal_code', 'address', 'email']
        widgets = {
            'customer_code': forms.TextInput(attrs={'placeholder': '得意先コード'}),
            'customer_name': forms.TextInput(attrs={'placeholder': '得意先名'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '電話番号'}),
            'postal_code': forms.TextInput(attrs={'placeholder': '郵便番号'}),
            'address': forms.TextInput(attrs={'placeholder': '住所'}),
            'email': forms.EmailInput(attrs={'placeholder': 'メールアドレス'}),
        }