from django import forms
from ..models import Shipment

class ShipmentFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '製品コード、製品名で検索'})
    )
    date_from = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    date_to = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    shipment_type = forms.ChoiceField(
        choices=[('', '全て')] + list(Shipment.SHIPMENT_TYPE_CHOICES),
        required=False
    )
