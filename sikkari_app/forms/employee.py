# forms/employee.py
from django import forms
from ..models import Employee

class EmployeeFilterForm(forms.Form):
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': '従業員番号、従業員名で検索'})
    )
    department_name = forms.ChoiceField(
        choices=[('', '全ての部署')] + [
            ('社長', '社長'),
            ('営業部', '営業部'),
            ('製造部', '製造部'),
            ('製品管理部', '製品管理部'),
            ('経理部', '経理部'),
            ('人事部', '人事部'),
        ],
        required=False
    )

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_code', 'employee_name', 'department_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }