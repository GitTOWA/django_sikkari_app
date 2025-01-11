# sikkari_app/urls.py
from django.urls import path, include
from .views.auth_views import LoginView, LogoutView
from .views.menu_views import MenuView
from .views.order_views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView
from .views.customer_views import CustomerListView, CustomerCreateView, CustomerUpdateView, CustomerDeleteView
from .views.production_views import Production, ProductionCreateView, ProductionFilterForm, ProductionForm, ProductionListView, ProductionUpdateView
from .views.product_views import Product, ProductCreateView, ProductDeleteView, ProductFilterForm, ProductForm, ProductListView, ProductUpdateView
from .views.stock_views import Stock, StockFilterForm, StockListView
from .views.shipment_views import Shipment, ShipmentFilterForm, ShipmentListView
from .views.employee_views import Employee, EmployeeCreateView, EmployeeDeleteView, EmployeeFilterForm, EmployeeForm, EmployeeListView, EmployeeUpdateView
from .views.department_views import Department, DepartmentCreateView, DepartmentDeleteView, DepartmentListView, DepartmentUpdateView

app_name = 'sikkari_app'

urlpatterns = []

# 認証管理
urlpatterns += [
  path('', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
]

# メニュー管理
urlpatterns += [
  path('menu/', MenuView.as_view(), name='menu'),
]

# 受注管理
urlpatterns += [
  path('orders/', OrderListView.as_view(), name='order_list'),
  path('orders/create/', OrderCreateView.as_view(), name='order_create'),
  path('orders/<int:pk>/update/', OrderUpdateView.as_view(), name='order_update'),
  path('orders/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),
]

# 顧客管理
urlpatterns += [
  path('customers/', CustomerListView.as_view(), name='customer_list'),
  path('customers/create/', CustomerCreateView.as_view(), name='customer_create'),
  path('customers/<int:pk>/update/', CustomerUpdateView.as_view(), name='customer_update'),
  path('customers/<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer_delete'),
]

# 生産管理
urlpatterns += [
  path('productions/', ProductionListView.as_view(), name='production_list'),
  path('productions/create/', ProductionCreateView.as_view(), name='production_create'),
  path('productions/<int:pk>/update/', ProductionUpdateView.as_view(), name='production_update'),
]

# 製品管理
urlpatterns += [
  path('products/', ProductListView.as_view(), name='product_list'),
  path('products/create/', ProductCreateView.as_view(), name='product_create'),
  path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
  path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]

# 在庫管理
urlpatterns += [
  path('stocks/', StockListView.as_view(), name='stock_list'),
]

# 入出荷管理
urlpatterns += [
  path('shipments/', ShipmentListView.as_view(), name='shipment_list'),
]

# 従業員管理
urlpatterns += [
  path('employees/', EmployeeListView.as_view(), name='employee_list'),
  path('employees/create/', EmployeeCreateView.as_view(), name='employee_create'),
  path('employees/<int:pk>/update/', EmployeeUpdateView.as_view(), name='employee_update'),
  path('employees/<int:pk>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
]

# 所属部署管理
urlpatterns += [
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),
]