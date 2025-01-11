# views/order_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from ..models import Order
from django import forms
from django.utils import timezone
from datetime import datetime, timedelta
from django.urls import reverse_lazy

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

class OrderListView(ListView):
    model = Order
    template_name = 'sikkari_app/order/list.html'
    context_object_name = 'orders'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        # フォームの取得とバリデーション
        form = OrderFilterForm(self.request.GET)
        print("Debug - Form data:", self.request.GET)  # デバッグ用

        if form.is_valid():
            # 検索クエリの処理
            search_query = form.cleaned_data.get('search')
            if search_query:
                print("Debug - Search query:", search_query)  # デバッグ用
                queryset = queryset.filter(
                    Q(order_code__icontains=search_query) |
                    Q(customer_name__icontains=search_query) |
                    Q(product_name__icontains=search_query)
                )

            # 日付範囲の処理
            date_from = form.cleaned_data.get('date_from')
            if date_from:
                queryset = queryset.filter(order_date__date__gte=date_from)

            date_to = form.cleaned_data.get('date_to')
            if date_to:
                queryset = queryset.filter(order_date__date__lte=date_to)

            # 配送状況の処理
            order_status = form.cleaned_data.get('order_status')
            if order_status == 'not_delivered':
                queryset = queryset.filter(delivery_date__isnull=True)
            elif order_status == 'delivered':
                queryset = queryset.filter(delivery_date__isnull=False)

        print("Debug - Final queryset:", queryset.query)  # デバッグ用
        return queryset.order_by('-order_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # フォームの初期値を現在のGETパラメータで設定
        context['filter_form'] = OrderFilterForm(self.request.GET or None)
        return context

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'sikkari_app/order/form.html'
    success_url = reverse_lazy('sikkari_app:order_list')  # パスを修正

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '受注情報登録'
        return context

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'sikkari_app/order/form.html'
    success_url = reverse_lazy('sikkari_app:order_list')  # パスを修正

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '受注情報更新'
        return context

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'sikkari_app/order/delete_confirm.html'
    success_url = reverse_lazy('sikkari_app:order_list')  # パスを修正

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '受注情報削除'
        return context