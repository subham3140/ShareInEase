from django.conf import settings
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = "shareApp"

urlpatterns = [
    path('loggedin/', views.login_user, name="loggedin"),
    path('loggedout/', views.logout_user, name="logout"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('createqr/', views.create_qrcode, name="createqr"),
    path('filedownload/<str:username>/<str:file>/<int:pk>/', views.filedownload, name="filedownload"),
]