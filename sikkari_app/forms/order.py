from django import forms
from ..models import Order

class OrderFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '受注コード、顧客名、製品名で検索'})
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    order_status = forms.ChoiceField(
        choices=[
            ('', '配送状況'),
            ('not_delivered', '未配送'),
            ('delivered', '配送済'),
        ],
        required=False
    )

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_code', 'customer_name', 'product_name', 'order_number', 
                 'order_date', 'expected_delivery_date', 'delivery_date']
        widgets = {
            'order_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'expected_delivery_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'delivery_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
