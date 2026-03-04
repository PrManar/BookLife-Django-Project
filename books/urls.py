from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('home/', views.home, name = 'home'),
  path('about/', views.about, name = 'about'),
  path('arabic/', views.arabic_books, name = 'arabic_books'),
  path('english/', views.english_books, name = 'english_books'),
  path('cbooks/', views.cbooks, name = 'cbooks'),
  path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
  path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
  path("register/", views.register_view, name="register"),
  path("cart/", views.cart_view, name="cart"),
  path("add-to-cart/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
  path("remove/<int:product_id>/", views.remove_from_cart, name="remove_from_cart"),
  path("clear-cart/", views.clear_cart, name="clear_cart"),
  path("checkout/", views.checkout, name="checkout"),
  path('profile/', views.profile, name='profile'),
  path('logout/', views.logout_view, name='logout')
]