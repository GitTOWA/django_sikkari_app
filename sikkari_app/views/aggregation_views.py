# views/aggregation_views.py
from django.views.generic import TemplateView
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.utils import timezone
from collections import defaultdict
from ..models import Order

class CustomerProductSummaryView(TemplateView):
    template_name = 'sikkari_app/aggregation/customer_product_summary.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # パラメータ取得
        view_type = self.request.GET.get('view_type', 'yearly')
        year = int(self.request.GET.get('year', timezone.now().year))
        month = self.request.GET.get('month', '')
        customer_name = self.request.GET.get('customer_name', '')
        product_name = self.request.GET.get('product_name', '')

        # クエリのデバッグ
        print("Debug - Parameters:", {
            'view_type': view_type,
            'year': year,
            'month': month,
            'customer_name': customer_name,
            'product_name': product_name
        })

        # 基本のクエリ
        queryset = Order.objects.filter(order_date__year=year)
        print("Debug - Initial Query Count:", queryset.count())

        if month and view_type == 'monthly':
            queryset = queryset.filter(order_date__month=month)
        if customer_name:
            queryset = queryset.filter(customer_name__icontains=customer_name)
        if product_name:
            queryset = queryset.filter(product_name__icontains=product_name)

        print("Debug - Final Query Count:", queryset.count())

        # 集計データの取得
        summary = self.get_yearly_summary(queryset) if view_type == 'yearly' else self.get_monthly_summary(queryset)
        print("Debug - Summary:", summary)

        context.update({
            'summary': summary,
            'view_type': view_type,
            'current_year': year,
            'current_month': month,
            'years': Order.objects.dates('order_date', 'year'),
            'months': range(1, 13),
            'filter_form': {
                'customer_name': customer_name,
                'product_name': product_name,
                'year': year,
                'month': month,
            }
        })
        return context

    def get_yearly_summary(self, queryset):
        """年次集計データを取得"""
        result = list(queryset.values(
            'customer_name', 
            'product_name'
        ).annotate(
            total_quantity=Sum('order_number'),
            order_count=Count('id')
        ).order_by('customer_name', 'product_name'))
        print("Debug - Yearly Summary:", result)
        return result

    def get_monthly_summary(self, queryset):
        """月次集計データを取得"""
        monthly_data = queryset.annotate(
            month=TruncMonth('order_date')
        ).values(
            'month', 
            'customer_name', 
            'product_name'
        ).annotate(
            total_quantity=Sum('order_number'),
            order_count=Count('id')
        ).order_by('month', 'customer_name', 'product_name')
        
        print("Debug - Monthly Raw Data:", monthly_data)

        # 月ごとにグループ化
        summary = defaultdict(list)
        for item in monthly_data:
            month = item['month'].month if item['month'] else 1
            summary[month].append({
                'customer_name': item['customer_name'],
                'product_name': item['product_name'],
                'total_quantity': item['total_quantity'],
                'order_count': item['order_count']
            })
        
        return dict(sorted(summary.items()))