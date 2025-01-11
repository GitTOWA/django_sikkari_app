from django.db import models
from django.utils.translation import gettext_lazy as _

class Department(models.Model):
    product_code = models.CharField(_('部署コード'), max_length=5)
    product_name = models.CharField(_('部署名'), max_length=10)

    class Meta:
        verbose_name = _('部署')
        verbose_name_plural = _('部署')

    def __str__(self):
        return self.product_name