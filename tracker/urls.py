from django.urls import path
from . import views
#from .views import DashboardView


urlpatterns = [
    path('', views.main, name='main'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('login/', views.login_request, name='login'),
    path('add_expense/', views.add_expense, name='add_expense'),
    #path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
