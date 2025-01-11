# Generated by Django 5.1.2 on 2025-01-10 11:46

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_code', models.CharField(max_length=5, unique=True, verbose_name='顧客コード')),
                ('customer_name', models.CharField(max_length=50, verbose_name='顧客名')),
                ('phone_number', models.CharField(max_length=11, verbose_name='電話番号')),
                ('postal_code', models.CharField(max_length=7, verbose_name='郵便番号')),
                ('address', models.CharField(max_length=50, verbose_name='住所')),
                ('email', models.EmailField(max_length=254, verbose_name='メールアドレス')),
            ],
            options={
                'verbose_name': '顧客',
                'verbose_name_plural': '顧客',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_code', models.CharField(max_length=5, unique=True, verbose_name='従業員コード')),
                ('employee_name', models.CharField(max_length=50, verbose_name='従業員名')),
                ('department_name', models.CharField(max_length=10, verbose_name='部署名')),
                ('password', models.CharField(max_length=128, verbose_name='パスワード')),
            ],
            options={
                'verbose_name': '従業員',
                'verbose_name_plural': '従業員',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_code', models.CharField(max_length=5, unique=True, verbose_name='注文コード')),
                ('customer_name', models.CharField(max_length=50, verbose_name='顧客名')),
                ('product_name', models.CharField(max_length=50, verbose_name='商品名')),
                ('order_number', models.IntegerField(verbose_name='注文数')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注文日')),
                ('expected_delivery_date', models.DateTimeField(verbose_name='予定納期')),
                ('delivery_date', models.DateTimeField(blank=True, null=True, verbose_name='実績納期')),
            ],
            options={
                'verbose_name': '注文',
                'verbose_name_plural': '注文',
            },
        ),
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=5, verbose_name='商品コード')),
                ('product_name', models.CharField(max_length=50, verbose_name='商品名')),
                ('lot_number', models.IntegerField(verbose_name='ロット番号')),
                ('order_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注文日')),
                ('manufacture_date', models.DateTimeField(verbose_name='製造開始日')),
                ('manufacture_completion_date', models.DateTimeField(verbose_name='製造完了日')),
            ],
            options={
                'verbose_name': '製造',
                'verbose_name_plural': '製造',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=5, unique=True, verbose_name='商品コード')),
                ('product_name', models.CharField(max_length=50, verbose_name='商品名')),
                ('stock_number', models.IntegerField(verbose_name='在庫数')),
            ],
            options={
                'verbose_name': '在庫',
                'verbose_name_plural': '在庫',
            },
        ),
    ]
