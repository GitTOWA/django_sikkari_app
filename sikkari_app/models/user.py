# models/user.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Employee(models.Model):
    employee_code = models.CharField(
        _('従業員コード'), 
        max_length=5, 
        unique=True
    )
    employee_name = models.CharField(
        _('従業員名'), 
        max_length=50
    )
    department_name = models.CharField(
        _('部署名'), 
        max_length=10
    )
    password = models.CharField(
        _('パスワード'), 
        max_length=128  # ハッシュ化されたパスワード用に長めに
    )

    class Meta:
        verbose_name = _('従業員')
        verbose_name_plural = _('従業員')

    def __str__(self):
        return f"{self.employee_code} - {self.employee_name}"