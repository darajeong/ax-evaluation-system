from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),

    # 우리가 만든 로그인/로그아웃
    path("", include("accounts.urls")),

    # django-allauth / Google 로그인
    path("accounts/", include("allauth.urls")),
]