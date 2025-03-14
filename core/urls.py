from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('users.urls')),
    path('register/', TemplateView.as_view(template_name='auth/register.html')),
    path('login/', TemplateView.as_view(template_name='auth/login.html')), 
    path('profile/', TemplateView.as_view(template_name='users/profile.html')),
]