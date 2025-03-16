from django.contrib import admin
from django.urls import path, include
from users.views import ZLoginView, ZSignupView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', ZLoginView.as_view(), name='login'),
    path('signup/', ZSignupView.as_view(), name='signup'),
    #path('api/', include('feed.api.urls')),  # Rotas DRF
]