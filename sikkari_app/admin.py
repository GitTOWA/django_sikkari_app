# admin.py
from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Employee, Stock, Order, Customer, Production, Department, Product, Shipment

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_code', 'employee_name', 'department_name')
    search_fields = ('employee_code', 'employee_name')
    list_filter = ('department_name',)

    def save_model(self, request, obj, form, change):
        if obj.password and not obj.password.startswith('pbkdf2_sha256'):
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

# GUIでDB確認 モデルの登録
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(Customer)
admin.site.register(Production)
admin.site.register(Department)
admin.site.register(Product)
admin.site.register(Shipment)