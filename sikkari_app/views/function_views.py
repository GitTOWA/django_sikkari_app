# views/function_views.py
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

class FunctionView(TemplateView):
    template_name = 'sikkari_app/function.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        system_name = kwargs.get('system_name')
        function_name = kwargs.get('function_name')
        
        # アクセス権限の確認
        department = self.request.session.get('department_name')
        if not self.has_access_permission(department, system_name, function_name):
            raise PermissionDenied
        
        context.update({
            'system_name': system_name,
            'function_name': function_name,
            'department_name': department,
            'employee_name': self.request.session.get('employee_name')
        })
        return context

    def has_access_permission(self, department, system_name, function_name):
        # アクセス権限チェックのロジック
        # MenuViewのdepartment_systemsと同じ構造で権限チェック
        return True  # 実際の権限チェックロジックを実装する

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('employee_id'):
            return redirect('sikkari_app:login')
        return super().dispatch(request, *args, **kwargs)