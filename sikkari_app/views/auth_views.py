# views/auth_views.py
from django.views.generic import FormView, RedirectView
from django.contrib.auth.hashers import check_password
from django.shortcuts import redirect
from django.urls import reverse_lazy
from sikkari_app.models import Employee
from sikkari_app.forms.auth import LoginForm  # パスを修正

class LoginView(FormView):
    template_name = 'sikkari_app/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('sikkari_app:menu')

    def dispatch(self, request, *args, **kwargs):
        # ログインページにアクセスした時点でセッションをクリア
        request.session.flush()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        employee_code = form.cleaned_data['employee_code']
        password = form.cleaned_data['password']
        try:
            employee = Employee.objects.get(employee_code=employee_code)
            if check_password(password, employee.password):
                self.request.session['employee_id'] = employee.id
                self.request.session['employee_name'] = employee.employee_name
                self.request.session['department_name'] = employee.department_name
                return super().form_valid(form)
        except Employee.DoesNotExist:
            pass
        
        form.add_error(None, '従業員番号またはパスワードが違います')
        return self.form_invalid(form)

class LogoutView(RedirectView):
    url = reverse_lazy('sikkari_app:login')

    def get(self, request, *args, **kwargs):
        request.session.flush()
        return super().get(request, *args, **kwargs)