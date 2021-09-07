from django.contrib.auth import views as auth_views


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
    # Reset Password
    path(
        'reset_password/',
        auth_views.PasswordResetView.as_view(template_name="post/password_reset.html"),
        name='reset_password',
    ),
    path(
        'reset_password_sent/',
        auth_views.PasswordResetDoneView.as_view(
            template_name="post/password_reset_sent.html"
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name="post/password_reset_form.html"
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset_password_complete/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name="post/password_reset_done.html"
        ),
        name='password_reset_complete',
    ),
]
