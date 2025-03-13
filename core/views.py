from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Главная страница
@login_required
def dashboard(request):
    return render(request, 'core/dashboard.html')

# Авторизация
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'core/login.html', {'error': 'Неверные данные'})
    return render(request, 'core/login.html')

# Выход
def logout_view(request):
    logout(request)
    return redirect('login')

# Дашборд студента
@login_required
def student_dashboard(request):
    return render(request, 'core/student/student_dashboard.html')

# Дашборд учителя
@login_required
def teacher_dashboard(request):
    return render(request, 'core/teacher/teacher_dashboard.html')

# Дашборд администратора
@login_required
def admin_dashboard(request):
    return render(request, 'core/admin/admin_dashboard.html')

# План учителя
@login_required
def teacher_plan(request):
    return render(request, 'core/teacher_plan.html')

# Редирект после входа
@login_required
def redirect_user(request):
    user = request.user
    if user.is_superuser:
        return redirect('core/admin/admin_dashboard.html')
    elif user.groups.filter(name='Teachers').exists():
        return redirect('core/teacher/teacher_dashboard.html')
    else:
        return redirect('core/student/student_dashboard')