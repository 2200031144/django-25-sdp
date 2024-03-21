from django.urls import path
from . import views

book = 'book'  # Replace 'your_app_name' with the name of your app

urlpatterns = [
    path('', views.home, name='home'),
    path('books/', views.books, name='books'),
    path('home1/', views.home1, name='home1'),
    path('login/', views.user_login, name='login'),
    path('cart/', views.cart_view, name='cart'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('index/', views.index, name='index'),
    path('checkout/', views.checkout_view, name='checkout'),
]