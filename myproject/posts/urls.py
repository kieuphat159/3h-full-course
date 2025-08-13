from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name="list"),
    path('new-post/', views.post_new, name="new-post"), 
    path('like/<int:post_id>/', views.like_post, name="like-post"),
    path('edit/<int:post_id>/', views.edit_post, name="edit-post"),
    path('delete/<int:post_id>/', views.delete_post, name="delete-post"),
    path('delete-confirm/<int:post_id>/', views.delete_post, name="confirm-delete"),
    path('<slug:slug>/', views.post_page, name="page"),
]
