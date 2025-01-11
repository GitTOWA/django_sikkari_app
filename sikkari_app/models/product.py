from django.db import models
from django.utils.translation import gettext_lazy as _

class Product(models.Model):
    product_code = models.CharField(_('製品コード'), max_length=5)
    product_name = models.CharField(_('製品名'), max_length=50)
    unit_price = models.IntegerField(_('製品単価'))

    class Meta:
        verbose_name = _('製品')
        verbose_name_plural = _('製品')

    def __str__(self):
        return f"{self.product_name} (Price: {self.unit_price})"