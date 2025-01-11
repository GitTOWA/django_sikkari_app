# views/employee_views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from ..models import Employee
from ..forms.employee import EmployeeForm, EmployeeFilterForm

class EmployeeListView(ListView):
    model = Employee
    template_name = 'sikkari_app/employee/list.html'
    context_object_name = 'employees'
    paginate_by = 10

    def get_queryset(self):
        queryset = Employee.objects.all()
        form = EmployeeFilterForm(self.request.GET)
        
        if form.is_valid():
            search_query = form.cleaned_data.get('search')
            if search_query:
                queryset = queryset.filter(
                    Q(employee_code__icontains=search_query) |
                    Q(employee_name__icontains=search_query)
                )

            department_name = form.cleaned_data.get('department_name')
            if department_name:
                queryset = queryset.filter(department_name=department_name)

        return queryset.order_by('employee_code')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = EmployeeFilterForm(self.request.GET or None)
        return context

class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'sikkari_app/employee/form.html'
    success_url = reverse_lazy('sikkari_app:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '従業員登録'
        return context

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.password = make_password(employee.password)
        employee.save()
        return super().form_valid(form)

class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'sikkari_app/employee/form.html'
    success_url = reverse_lazy('sikkari_app:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '従業員更新'
        return context

    def form_valid(self, form):
        employee = form.save(commit=False)
        if 'password' in form.changed_data:
            employee.password = make_password(employee.password)
        employee.save()
        return super().form_valid(form)

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'sikkari_app/employee/delete_confirm.html'
    success_url = reverse_lazy('sikkari_app:employee_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '従業員削除'
        return context