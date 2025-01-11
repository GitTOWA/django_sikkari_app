# sikkari_app/views/__init__.py
from .auth_views import LoginView, LogoutView
from .menu_views import MenuView
from .function_views import FunctionView
from .order_views import Order, OrderForm, OrderCreateView, OrderDeleteView, OrderFilterForm, OrderListView, OrderUpdateView
from .customer_views import CreateView, Customer, CustomerCreateView, CustomerDeleteView, CustomerFilterForm, CustomerForm, CustomerListView, CustomerUpdateView
from .employee_views import Employee, EmployeeCreateView, EmployeeDeleteView, EmployeeFilterForm, EmployeeForm, EmployeeListView, EmployeeUpdateView
from .product_views import Product, ProductCreateView, ProductDeleteView, ProductFilterForm, ProductForm, ProductListView, ProductUpdateView
from .production_views import Production, ProductionCreateView, ProductionFilterForm, ProductionForm, ProductionListView, ProductionUpdateView
from .shipment_views import Shipment, ShipmentFilterForm, ShipmentListView
from .stock_views import Stock, StockFilterForm, StockListView

__all__ = []

# Auth Views
__all__ += [
    'LoginView',
    'LogoutView'
]

# Menu Views
__all__ += [
    'MenuView'
]

# Function Views
__all__ += [
    'FunctionView'
]

# Order Views
__all__ += [
    'Order',
    'OrderForm',
    'OrderCreateView',
    'OrderDeleteView',
    'OrderFilterForm',
    'OrderListView',
    'OrderUpdateView'
]

# Customer Views
__all__ += [
    'CreateView',
    'Customer',
    'CustomerCreateView',
    'CustomerDeleteView',
    'CustomerFilterForm',
    'CustomerForm',
    'CustomerListView',
    'CustomerUpdateView'
]

# Employee Views
__all__ += [
    'Employee',
    'EmployeeCreateView',
    'EmployeeDeleteView',
    'EmployeeFilterForm',
    'EmployeeForm',
    'EmployeeListView',
    'EmployeeUpdateView'
]

# Product Views
__all__ += [
    'Product',
    'ProductCreateView',
    'ProductDeleteView',
    'ProductFilterForm',
    'ProductForm',
    'ProductListView',
    'ProductUpdateView'
]

# Production Views
__all__ += [
    'Production',
    'ProductionCreateView',
    'ProductionFilterForm',
    'ProductionForm',
    'ProductionListView',
    'ProductionUpdateView'
]

# Shipment Views
__all__ += [
    'Shipment',
    'ShipmentFilterForm',
    'ShipmentListView'
]

# Stock Views
__all__ += [
    'Stock',
    'StockFilterForm',
    'StockListView'
]
