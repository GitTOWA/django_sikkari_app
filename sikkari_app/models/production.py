# models/production.py
from django.db import models
from django.utils.translation import gettext_lazy as _

class Production(models.Model):
    STATUS_CHOICES = (
        ('pending', '未着手'),
        ('in_progress', '進行中'),
        ('completed', '完了')
    )

    product_code = models.CharField(_('製品コード'), max_length=5)
    product_name = models.CharField(_('製品名'), max_length=50)
    lot_number = models.IntegerField(_('ロット番号'))
    order_date = models.DateTimeField(_('注文日'))
    manufacture_date = models.DateTimeField(_('製造開始日'))
    manufacture_completion_date = models.DateTimeField(_('製造完了予定日'))
    actual_completion_date = models.DateTimeField(_('実績完了日'), null=True, blank=True)
    status = models.CharField(
        _('状態'),
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    class Meta:
        verbose_name = _('製造')
        verbose_name_plural = _('製造')

    def __str__(self):
        return f"{self.product_name} (Lot: {self.lot_number})"