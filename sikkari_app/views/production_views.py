# views/production_views.py
from django.views.generic import ListView, CreateView, UpdateView
from django.db.models import Q
from django.urls import reverse_lazy
from django.utils import timezone
from ..models import Production
from ..forms import ProductionForm, ProductionFilterForm 

class ProductionListView(ListView):
    model = Production
    template_name = 'sikkari_app/production/list.html'
    context_object_name = 'productions'
    paginate_by = 10

    def get_queryset(self):
        queryset = Production.objects.all()
        form = ProductionFilterForm(self.request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            if search_query:
                queryset = queryset.filter(
                    Q(product_code__icontains=search_query) |
                    Q(product_name__icontains=search_query)
                )

            date_from = form.cleaned_data.get('date_from')
            if date_from:
                queryset = queryset.filter(order_date__date__gte=date_from)

            date_to = form.cleaned_data.get('date_to')
            if date_to:
                queryset = queryset.filter(order_date__date__lte=date_to)

            # 完了済み表示の制御
            if not form.cleaned_data.get('show_completed', False):
                queryset = queryset.filter(manufacture_completion_date__gt=timezone.now())

        return queryset.order_by('-order_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = ProductionFilterForm(self.request.GET or None)
        return context

class ProductionCreateView(CreateView):
    model = Production
    form_class = ProductionForm
    template_name = 'sikkari_app/production/form.html'
    success_url = reverse_lazy('sikkari_app:production_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '生産情報登録'
        return context

class ProductionUpdateView(UpdateView):
    model = Production
    form_class = ProductionForm
    template_name = 'sikkari_app/production/form.html'
    success_url = reverse_lazy('sikkari_app:production_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '生産情報更新'
        return context