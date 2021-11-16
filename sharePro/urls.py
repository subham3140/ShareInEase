from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('shareApp/', include('shareApp.urls', namespace="shareApp")),
    path('', views.home, name="home"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('login/', TemplateView.as_view(template_name = 'login/login.html'), name="login"),
    path('profile/',views.profile, name="profile"),
    path('register/', views.register, name="register"),
    path('admin/', admin.site.urls),
    path('checkqrcode/', views.checkqrcode, name="checkqrcode"),
    url(r'download/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
