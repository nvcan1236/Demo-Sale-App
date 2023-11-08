from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Category, Product
from flask_admin import BaseView, expose

admin = Admin(app=app, template_mode='bootstrap4', name='QUẢN TRỊ BÁN HÀNG')


class MyCategoryView(ModelView):
    create_modal = True
    column_list = ['name', 'products']


class MyProductView(ModelView):
    column_list = ['name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    create_modal = True
    column_editable_list = ['name', 'price']


class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/stats.html')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(StatsView(name='Báo cáo thống kê'))
