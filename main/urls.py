from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('registration/', views.UserFormView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]

