from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="index"),
    #path("login", views.login_view, name="login"),
    #path("logout", views.logout_view, name="logout"),

    path('signup/', views.SignUp.as_view(), name='signup'),
    #path("register", views.register_view, name="register")
]
