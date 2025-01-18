# views/history_views.py
from django.views.generic import ListView
from django.db.models import Q
from ..models import Order
from django.utils import timezone

class OrderHistoryView(ListView):
    template_name = 'sikkari_app/history/order_history.html'
    model = Order
    context_object_name = 'orders'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 検索パラメータ取得
        context['customer_name'] = self.request.GET.get('customer_name', '')
        context['product_name'] = self.request.GET.get('product_name', '')
        context['date_from'] = self.request.GET.get('date_from', '')
        context['date_to'] = self.request.GET.get('date_to', '')
        
        # ユニークな得意先名と製品名のリストを取得
        context['customer_list'] = Order.objects.values_list('customer_name', flat=True).distinct()
        context['product_list'] = Order.objects.values_list('product_name', flat=True).distinct()
        
        return context

    def get_queryset(self):
        queryset = Order.objects.all().order_by('-order_date')
        
        # 検索フィルタの適用
        customer_name = self.request.GET.get('customer_name')
        if customer_name:
            queryset = queryset.filter(customer_name=customer_name)

        product_name = self.request.GET.get('product_name')
        if product_name:
            queryset = queryset.filter(product_name=product_name)

        date_from = self.request.GET.get('date_from')
        if date_from:
            queryset = queryset.filter(order_date__gte=date_from)

        date_to = self.request.GET.get('date_to')
        if date_to:
            queryset = queryset.filter(order_date__lte=date_to)

        return queryset