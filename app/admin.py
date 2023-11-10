from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Category, Product, User, UserRole
from flask_admin import BaseView, expose
from flask_login import logout_user, current_user
from flask import redirect, url_for

admin = Admin(app=app, template_mode='bootstrap4', name='QUẢN TRỊ BÁN HÀNG')


class AdminAuthModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class ShopView(BaseView):
    @expose('/')
    def index(self):
        return redirect(url_for('index'))


class MyCategoryView(AdminAuthModelView):
    create_modal = True
    column_list = ['name', 'products']


class MyProductView(AdminAuthModelView):
    column_list = ['name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    create_modal = True
    column_editable_list = ['name', 'price']


class MyUserView(AdminAuthModelView):
    pass


class AuthBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class StatsView(AuthBaseView):
    @expose('/')
    def index(self):
        return self.render('/admin/stats.html')


class LogoutView(AuthBaseView):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')


admin.add_view(ShopView(name='Trang bán hàng'))
admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyUserView(User, db.session))
admin.add_view(StatsView(name='Báo cáo thống kê'))
admin.add_view(LogoutView(name='Đăng xuất'))
