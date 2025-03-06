from django.urls import path
from core import views  

urlpatterns = [
    # Главная страница
    path('', views.dashboard, name='home'),

    # Авторизация
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Дашборды для разных ролей
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/student/', views.student_dashboard, name='student_dashboard'),
    path('dashboard/teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),

    # Редирект после входа
    path('redirect-user/', views.redirect_user, name='redirect_user'),
]
