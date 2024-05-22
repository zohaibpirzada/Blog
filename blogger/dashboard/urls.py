from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('all-post/', views.all_post, name='all_post'),
    path('my-post/', views.my_post, name='my_post'),
    path('all-categories/', views.all_categories, name='all_categories'),
    path('add-category/', views.add_category, name='add_category'),
    path('edit-category/<int:cat_id>/', views.edit_category, name='edit_category'),
    path('delete/category/<int:cat_id>', views.delete_cat, name='delete_cat'),
    path('category/sets/<int:cat_id>', views.cat_set, name='cat_set'),
    path('post/edit/<int:post_id>', views.edit_post, name='edit_post'),
    path('delete/post/<int:post_id>', views.delete_post, name='delete_post'),
]
