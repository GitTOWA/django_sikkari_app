# views/customer_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from django.urls import reverse_lazy
from ..models import Customer
from django import forms

# フィルターフォーム
class CustomerFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '得意先コード、得意先名で検索'})
    )

# 得意先情報フォーム
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_code', 'customer_name', 'phone_number', 
                 'postal_code', 'address', 'email']
        widgets = {
            'customer_code': forms.TextInput(attrs={'placeholder': '得意先コード'}),
            'customer_name': forms.TextInput(attrs={'placeholder': '得意先名'}),
            'phone_number': forms.TextInput(attrs={'placeholder': '電話番号'}),
            'postal_code': forms.TextInput(attrs={'placeholder': '郵便番号'}),
            'address': forms.TextInput(attrs={'placeholder': '住所'}),
            'email': forms.EmailInput(attrs={'placeholder': 'メールアドレス'}),
        }

# 一覧表示
class CustomerListView(ListView):
    model = Customer
    template_name = 'sikkari_app/customer/list.html'
    context_object_name = 'customers'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = CustomerFilterForm(self.request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            if search_query:
                queryset = queryset.filter(
                    Q(customer_code__icontains=search_query) |
                    Q(customer_name__icontains=search_query)
                )
        return queryset.order_by('customer_code')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = CustomerFilterForm(self.request.GET or None)
        return context

# 新規作成
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sikkari_app/customer/form.html'
    success_url = reverse_lazy('sikkari_app:customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '得意先情報登録'
        return context

# 更新
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'sikkari_app/customer/form.html'
    success_url = reverse_lazy('sikkari_app:customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '得意先情報更新'
        return context

# 削除
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'sikkari_app/customer/delete_confirm.html'
    success_url = reverse_lazy('sikkari_app:customer_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '得意先情報削除'
        return context