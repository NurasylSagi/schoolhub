from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')

@login_required
def admin_dashboard(request):
    return render(request, 'core/admin_dashboard.html')

from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def redirect_user(request):
    user = request.user
    if user.role == 'admin':
        return redirect('admin_dashboard')
    elif user.role == 'teacher':
        return redirect('teacher_dashboard')
    else:
        return redirect('student_dashboard')
from django.shortcuts import render

def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")  # Перенаправление после входа
        else:
            return render(request, "core/login.html", {"error": "Неверные данные"})

    return render(request, "core/login.html")

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def dashboard(request):
    return render(request, "core/dashboard.html")  # Общая панель


from django.views.generic import TemplateView

class DashboardView(TemplateView):
    template_name = "core/dashboard.html"  # Путь к шаблону


from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    return render(request, 'core/student_dashboard.html')


@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher_dashboard.html')

@login_required
def schedule_dashboard(request):
    return render(request, 'core/schedule_dashboard.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')  # Путь к шаблону
    

from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")