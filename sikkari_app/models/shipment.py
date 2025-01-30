from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

class Shipment(models.Model):
    SHIPMENT_TYPE_CHOICES = (
        ('in', '入荷'),
        ('out', '出荷'),
    )

    product_code = models.CharField(_('製品コード'), max_length=5)
    product_name = models.CharField(_('製品名'), max_length=50)
    quantity = models.IntegerField(_('数量'))
    shipment_type = models.CharField(_('区分'), max_length=3, choices=SHIPMENT_TYPE_CHOICES)
    shipment_date = models.DateTimeField(_('入出荷日'), default=timezone.now)
    
    class Meta:
        verbose_name = _('入出荷')
        verbose_name_plural = _('入出荷')
        ordering = ['-shipment_date']

    def __str__(self):
        return f"{self.get_shipment_type_display()}: {self.product_name} ({self.quantity})"