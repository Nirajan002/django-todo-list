from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_task, name='add'),
    path('delete/<int:task_id>/', views.delete_task, name='delete'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('update/<int:id>/', views.update_task, name='update_task'),
]
