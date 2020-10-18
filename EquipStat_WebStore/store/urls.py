from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('user/<str:pk>', views.profile, name='profile'),
    path('store/', views.store, name="store"),
    path('store/<slug:slug>/', views.product, name="product"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('product/', views.product, name="product"),
]

