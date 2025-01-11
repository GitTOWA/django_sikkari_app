# forms/production.py
from django import forms
from ..models import Production

class ProductionFilterForm(forms.Form):
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
    status = forms.ChoiceField(
        choices=(('', '全ての状態'),) + Production.STATUS_CHOICES,  # タプルに変更
        required=False
    )
    show_completed = forms.BooleanField(
        required=False,
        label='完了済みを含む',
        initial=False
    )

class ProductionForm(forms.ModelForm):
    class Meta:
        model = Production
        fields = [
            'product_code', 'product_name', 'lot_number', 
            'order_date', 'manufacture_date', 'manufacture_completion_date',
            'actual_completion_date', 'status'
        ]
        widgets = {
            'order_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'manufacture_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'manufacture_completion_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'actual_completion_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }