from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("login/success/", views.login_success, name="login_success"),
    path("logout/", views.logout_view, name="logout"),
    path("admin-page/", views.admin_page, name="admin_page"),
]