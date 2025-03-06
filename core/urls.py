from django.urls import path
from django.contrib.auth.decorators import login_required
from core import views  

urlpatterns = [
    path('', views.dashboard, name='home'),  # Главная страница ведёт на дашборд
    path('dashboard/', views.dashboard, name='dashboard'),
    
    # Авторизация
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Дашборды для разных типов пользователей
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),

    # Редирект после входа
    path('redirect-user/', views.redirect_user, name='redirect_user'),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # Подключаем маршруты из core
]

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
