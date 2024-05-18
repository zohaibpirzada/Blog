from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('register/', views.user_sign, name='register'),
    path('profile/edit/', views.edit_profile, name='edit'),
    path('add-blog/', views.add_blog, name='add_blog'),
    path('add-category/', views.Add_cat, name='add_cat'),
]
