from django.urls import path
from .Views import cpl_views, tsk_views, base_views


app_name = 'complaints'
urlpatterns = [
    path('', base_views.index, name='index'),
    path('dashboard/', base_views.dashboard, name='dashboard')
    ]
