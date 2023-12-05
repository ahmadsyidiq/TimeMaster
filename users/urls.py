from django.urls import path
from . import views


urlpatterns = [
    path('register', views.registration, name = 'register'),
    path('login', views.UserLoginView.as_view(), name = 'login'),
    path('logout', views.logout_user, name = 'logout'),
    path('update-profile', views.update_profile, name ='update-profile'),
]