from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = 'core_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='core_app/login.html'), name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('register/', views.register_customer, name='register'),
    path('dashboard/', views.citizen_dashboard, name='citizen_dashboard'),
    path('complaints/new/', views.create_complaint, name='complaint_create'),
    path('manager/', views.manager_dashboard, name='manager_dashboard'),
    path('complaints/', views.complaint_list, name='complaint_list'),
    path('complaints/<int:pk>/', views.complaint_detail, name='complaint_detail'),
]
