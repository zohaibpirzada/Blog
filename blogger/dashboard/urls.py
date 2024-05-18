from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('all-post/', views.all_post, name='all_post'),
    path('my-post/', views.my_post, name='my_post'),
    path('all-categories/', views.all_categories, name='all_categories'),
]
