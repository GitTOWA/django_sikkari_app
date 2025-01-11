# views/stock_views.py
from django.views.generic import ListView
from django.db.models import Q
from ..models import Stock
from ..forms import StockFilterForm

class StockListView(ListView):
    model = Stock
    template_name = 'sikkari_app/stock/list.html'
    context_object_name = 'stocks'
    paginate_by = 10

    def get_queryset(self):
        queryset = Stock.objects.all()
        form = StockFilterForm(self.request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            if search_query:
                queryset = queryset.filter(
                    Q(product_code__icontains=search_query) |
                    Q(product_name__icontains=search_query)
                )

            stock_min = form.cleaned_data.get('stock_min')
            if stock_min is not None:
                queryset = queryset.filter(stock_number__gte=stock_min)

            stock_max = form.cleaned_data.get('stock_max')
            if stock_max is not None:
                queryset = queryset.filter(stock_number__lte=stock_max)

        return queryset.order_by('product_code')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = StockFilterForm(self.request.GET or None)
        return context