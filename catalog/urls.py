from django.conf.urls import url
from django.urls import path, re_path
from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.products_list, name='product_list'),
    path('<slug:slug>/', views.category, name='category'),
    path('produtos/<slug:slug>/', views.product, name='product'),
]

