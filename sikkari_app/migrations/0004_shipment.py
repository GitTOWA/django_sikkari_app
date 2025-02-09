# Generated by Django 5.1.2 on 2025-01-11 07:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sikkari_app', '0003_production_actual_completion_date_production_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=5, verbose_name='製品コード')),
                ('product_name', models.CharField(max_length=50, verbose_name='製品名')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('shipment_type', models.CharField(choices=[('in', '入荷'), ('out', '出荷')], max_length=3, verbose_name='区分')),
                ('shipment_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='入出荷日')),
            ],
            options={
                'verbose_name': '入出荷',
                'verbose_name_plural': '入出荷',
                'ordering': ['-shipment_date'],
            },
        ),
    ]
