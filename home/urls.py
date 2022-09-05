from django.urls import path
from . import views

urlpatterns = [
    path('' , views.Homeview.as_view()),
    path('authorized',views.Authorizedview.as_view()),
    path('login',views.LoginInterfaceView.as_view(), name='login'),
    path('logout',views.LogoutInterfaceView.as_view(), name='logout'),
    path('signup',views.SignupView.as_view(), name='signup'),
]