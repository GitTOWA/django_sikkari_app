# forms/product.py
from django import forms
from ..models import Product

class ProductFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '製品コード、製品名で検索'})
    )
    price_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '最小価格'})
    )
    price_max = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '最大価格'})
    )

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_code', 'product_name', 'unit_price']
        widgets = {
            'product_code': forms.TextInput(attrs={'placeholder': '製品コード'}),
            'product_name': forms.TextInput(attrs={'placeholder': '製品名'}),
            'unit_price': forms.NumberInput(attrs={'placeholder': '製品単価'})
        }