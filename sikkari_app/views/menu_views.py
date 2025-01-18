# views/menu_views.py
from django.views.generic import TemplateView
from django.shortcuts import redirect

class MenuView(TemplateView):
    template_name = 'sikkari_app/menu/menu.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.request.session.get('department_name')

        # 部署ごとのアクセス可能システムと機能を定義
        department_systems = {
            '営業部': {
                '販売支援システム': [
                    {'name': '受注情報', 'url': 'order_list'},
                    {'name': '得意先情報', 'url': 'customer_list'},
                    {'name': '得意先・製品別集計', 'url': 'customer_product_summary'},
                    {'name': '得意先・商品別履歴', 'url': 'order_history'}
                ],
                '製品管理システム': [
                    {'name': '生産管理', 'url': 'production_list'},
                    {'name': '製品管理', 'url': 'product_list'},
                    {'name': '在庫管理', 'url': 'stock_list'},
                    {'name': '入出荷管理', 'url': 'shipment_list'}
                ]
            },
            '人事部': {
                '従業員管理システム': [
                    {'name': '従業員情報', 'url': 'employee_list'},
                    {'name': '所属部署情報', 'url': 'department_list'}
                ]
            },
            '製造部': {
                '製品管理システム': [
                    {'name': '生産管理', 'url': 'production_list'},
                    {'name': '製品管理', 'url': 'product_list'},
                    {'name': '在庫管理', 'url': 'stock_list'},
                    {'name': '入出荷管理', 'url': 'shipment_list'}
                ]
            },
            '製品管理部': {
                '製品管理システム': [
                    {'name': '生産管理', 'url': 'production_list'},
                    {'name': '製品管理', 'url': 'product_list'},
                    {'name': '在庫管理', 'url': 'stock_list'},
                    {'name': '入出荷管理', 'url': 'shipment_list'}
                ]
            }
        }

        context['systems'] = department_systems.get(department, {})
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('employee_id'):
            return redirect('sikkari_app:login')
        return super().dispatch(request, *args, **kwargs)