from django.urls import path

from . import views


app_name = 'checkout'

urlpatterns = [
    path(
        'carrinho/adicionar/<slug:slug>/', views.create_cartItem, name='create_cartitem'
    ),
]
