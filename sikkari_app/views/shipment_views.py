# views/shipment_views.py
from django.views.generic import ListView
from django.db.models import Q
from ..models import Shipment
from ..forms.shipment import ShipmentFilterForm

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