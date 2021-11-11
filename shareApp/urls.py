from django.urls import path
from django.views.generic.base import TemplateView
from . import views
app_name = "shareApp"

urlpatterns = [
    path('loggedin/', views.login_user, name="loggedin"),
    path('loggedout/', views.logout_user, name="logout"),
    path('detail/<int:pk>', views.detail, name="detail")
]