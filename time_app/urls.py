from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("index.html", views.index),    
    path("login/", views.myLoginView.as_view(), name="login"),
    path("get_user_data", views.get_user_data, name="get_user_data"),
]