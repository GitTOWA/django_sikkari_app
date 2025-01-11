# views/department_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Department

class DepartmentListView(ListView):
    model = Department
    template_name = 'sikkari_app/department/list.html'
    context_object_name = 'departments'
    paginate_by = 10

    def get_queryset(self):
        return Department.objects.all().order_by('product_code')

class DepartmentCreateView(CreateView):
    model = Department
    template_name = 'sikkari_app/department/form.html'
    fields = ['product_code', 'product_name']
    success_url = reverse_lazy('sikkari_app:department_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '部署登録'
        return context

class DepartmentUpdateView(UpdateView):
    model = Department
    template_name = 'sikkari_app/department/form.html'
    fields = ['product_code', 'product_name']
    success_url = reverse_lazy('sikkari_app:department_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '部署更新'
        return context

class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'sikkari_app/department/delete_confirm.html'
    success_url = reverse_lazy('sikkari_app:department_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '部署削除'
        return context