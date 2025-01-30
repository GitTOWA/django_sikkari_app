# views/product_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from ..models import Product
from ..forms import ProductFilterForm, ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'sikkari_app/product/list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = Product.objects.all()
        # print("Debug - Products:", list(queryset))
        form = ProductFilterForm(self.request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            if search_query:
                queryset = queryset.filter(
                    Q(product_code__icontains=search_query) |
                    Q(product_name__icontains=search_query)
                )

            price_min = form.cleaned_data.get('price_min')
            if price_min is not None:
                queryset = queryset.filter(unit_price__gte=price_min)

            price_max = form.cleaned_data.get('price_max')
            if price_max is not None:
                queryset = queryset.filter(unit_price__lte=price_max)

        return queryset.order_by('product_code')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProductFilterForm(self.request.GET or None)
        # print("Debug - Context:", context)
        return context

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'sikkari_app/product/form.html'
    success_url = reverse_lazy('sikkari_app:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '製品登録'
        return context

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'sikkari_app/product/form.html'
    success_url = reverse_lazy('sikkari_app:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '製品更新'
        return context

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'sikkari_app/product/delete_confirm.html'
    success_url = reverse_lazy('sikkari_app:product_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '製品削除'
        return context