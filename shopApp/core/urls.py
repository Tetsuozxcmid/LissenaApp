from django.urls import path
from django.shortcuts import redirect
from . import views


urlpatterns = [
    path('', views.auth_home, name='auth_home'),
    path('categoty/<str:category_post>',views.category_view,name='category'),
    path('product/<int:post_id>/', views.product_detail, name='product_detail'),
]