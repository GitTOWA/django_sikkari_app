# views/shipment_views.py
from django.views.generic import ListView
from django.db.models import Q
from ..models import Shipment
from django import forms

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

class ShipmentListView(ListView):
    model = Shipment
    template_name = 'sikkari_app/shipment/list.html'
    context_object_name = 'shipments'
    paginate_by = 10

    def get_queryset(self):
        queryset = Shipment.objects.all()
        form = ShipmentFilterForm(self.request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            if search_query:
                queryset = queryset.filter(
                    Q(product_code__icontains=search_query) |
                    Q(product_name__icontains=search_query)
                )

            date_from = form.cleaned_data.get('date_from')
            if date_from:
                queryset = queryset.filter(shipment_date__date__gte=date_from)

            date_to = form.cleaned_data.get('date_to')
            if date_to:
                queryset = queryset.filter(shipment_date__date__lte=date_to)

            shipment_type = form.cleaned_data.get('shipment_type')
            if shipment_type:
                queryset = queryset.filter(shipment_type=shipment_type)

        return queryset.order_by('-shipment_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ShipmentFilterForm(self.request.GET or None)
        return context