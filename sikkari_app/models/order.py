from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Order(models.Model):
    order_code = models.CharField(_('注文コード'), max_length=5, unique=True)
    customer_name = models.CharField(_('顧客名'), max_length=50)
    product_name = models.CharField(_('商品名'), max_length=50)
    order_number = models.IntegerField(_('注文数'))
    order_date = models.DateTimeField(_('注文日'), default=timezone.now)
    expected_delivery_date = models.DateTimeField(_('予定納期'))
    delivery_date = models.DateTimeField(_('実績納期'), null=True, blank=True)

    class Meta:
        verbose_name = _('注文')
        verbose_name_plural = _('注文')

    def __str__(self):
        return f"Order {self.order_code} - {self.customer_name}"

class Customer(models.Model):
    customer_code = models.CharField(_('顧客コード'), max_length=5, unique=True)
    customer_name = models.CharField(_('顧客名'), max_length=50)
    phone_number = models.CharField(_('電話番号'), max_length=11)
    postal_code = models.CharField(_('郵便番号'), max_length=7)
    address = models.CharField(_('住所'), max_length=50)
    email = models.EmailField(_('メールアドレス'))

    class Meta:
        verbose_name = _('顧客')
        verbose_name_plural = _('顧客')

    def __str__(self):
        return self.customer_name