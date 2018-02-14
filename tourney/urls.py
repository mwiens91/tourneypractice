from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from tournaments import views

urlpatterns = [
    path(r'', views.home, name='home',),
    path('admin/', admin.site.urls),
    path(r'signup/',views.signup, name='signup'),
    path(r'tourney/<int:tourney_id>/', views.tourney, name='tourney'),
    path(r'login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path(r'logout/', auth_views.logout,{'next_page': '/'}, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)










