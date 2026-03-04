from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Product, Category

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')


def arabic_books(request):
    category = get_object_or_404(Category, name="Arabic")
    products = Product.objects.filter(category=category, available=True)

    return render(request, "arabic_books.html", {"products": products})

def english_books(request):
    category = get_object_or_404(Category, name="English")
    products = Product.objects.filter(category=category, available=True)

    return render(request, "english_books.html", {"products": products})

def cbooks(request):
    category = get_object_or_404(Category, name="Childrens")
    products = Product.objects.filter(category=category, available=True)

    return render(request, "cbooks.html", {"products": products})


from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after register
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})


def cart_view(request):
    cart = request.session.get('cart', {})
    products = Product.objects.filter(id__in=cart.keys())

    cart_items = []
    total = 0

    for product in products:
        quantity = cart[str(product.id)]
        total_price = product.price * quantity
        total += total_price

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_price': total_price
        })

    return render(request, "cart.html", {
        "cart_items": cart_items,
        "total": total
    })

from django.contrib import messages

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1

    request.session['cart'] = cart
    messages.success(request, "Book added to cart successfully!")

    return redirect(request.META.get('HTTP_REFERER', 'home'))

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})

    if str(product_id) in cart:
        del cart[str(product_id)]

    request.session['cart'] = cart
    return redirect('cart')

def clear_cart(request):
    request.session['cart'] = {}
    return redirect('cart')

def checkout(request):
    request.session['cart'] = {}  # clear cart after purchase
    return render(request, "checkout_success.html")

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect('home') 

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def profile(request):
    return render(request, 'profile.html')