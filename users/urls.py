from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('upload/', views.upload_view, name='upload'),
    path('contact/', views.contact_view, name='contact'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/editprofile/<int:pk>/', views.UpdateProfileView.as_view(), name='editprofile'),

]