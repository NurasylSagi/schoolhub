from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),  # Обязательно добавляем эту строку
    path("", include("core.urls")),  # Подключаем маршруты из core
]



from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Импортируем встроенные представления аутентификации

urlpatterns = [
    path("admin/", admin.site.urls),  
    path("", include("core.urls")),  
    path("login/", auth_views.LoginView.as_view(), name="login"),  # <-- Добавляем URL для логина
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),  # <-- Добавляем URL для выхода
]


from django.urls import path
from core import views  # Убедись, что `views` импортирован правильно

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),  # Добавляем этот маршрут
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]


from django.urls import path
from core import views  # Импортируем представления из core

urlpatterns = [
    path("admin/", admin.site.urls),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('student/', views.logout_view, name='student'),

    
    # Добавляем маршрут для главной страницы
    path("", views.dashboard, name="home"),  # Можно перенаправить на dashboard
]
