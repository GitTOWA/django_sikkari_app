from django.db import models
from django.utils.translation import gettext_lazy as _

class Stock(models.Model):
    product_code = models.CharField(_('商品コード'), max_length=5, unique=True)
    product_name = models.CharField(_('商品名'), max_length=50)
    stock_number = models.IntegerField(_('在庫数'))

    class Meta:
        verbose_name = _('在庫')
        verbose_name_plural = _('在庫')

    def __str__(self):
        return f"{self.product_name} ({self.stock_number})"