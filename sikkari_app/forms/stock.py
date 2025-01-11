# forms/stock.py
from django import forms

class StockFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '製品コード、製品名で検索'})
    )
    stock_min = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '最小在庫数'})
    )
    stock_max = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(attrs={'placeholder': '最大在庫数'})
    )