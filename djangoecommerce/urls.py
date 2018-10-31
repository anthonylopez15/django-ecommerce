
from django.contrib import admin
from django.urls import path, include
from core import views
from catalog import urls as catalog_urls
from accounts import ulrs as accounts_urls
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('contato/', views.contact, name='contact'),
    path('entrar/', LoginView.as_view(template_name='login.html'), name="login"),
    path('sair/', LogoutView.as_view(next_page='/'), name="logout"),
    path('catalogo/', include(catalog_urls)),
    path('conta/', include(accounts_urls)),
    path('admin/', admin.site.urls),
]
