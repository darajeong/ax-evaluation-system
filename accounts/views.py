from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("login_success")

        return render(
            request,
            "accounts/login.html",
            {"error": "아이디 또는 비밀번호가 올바르지 않습니다."},
        )

    return render(request, "accounts/login.html")


@login_required
def login_success(request):
    return render(request, "accounts/login_success.html")
def logout_view(request):
    logout(request)
    return redirect("login")

def is_admin(user):
    return user.is_staff


@user_passes_test(is_admin, login_url="/login/")
def admin_page(request):
    return render(request, "accounts/admin_page.html")