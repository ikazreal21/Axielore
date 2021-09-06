from django.urls import path
from . import views


urlpatterns = [
    # User
    path('register/', views.Register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    # App
    path('', views.PostFeed, name='index'),
    path('create_post', views.CreatePost, name="createpost"),
    path("update/<str:pk>", views.UpdatePost, name="update"),
    path("delete/<str:pk>", views.DeletePost, name="delete"),
]
