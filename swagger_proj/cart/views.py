from django.contrib.auth import user_logged_out
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
# from swagger_proj.films import models
from films import models

# def cart_index(request):
#     return render(request, 'cart_index.html', {})

@require_POST
def cart_add(request, film_id):
    cart = Cart(request)

    product = get_object_or_404(models.Film, id=film_id)

    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data # данные из формы

        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return redirect('cart:cart_detail')

def cart_remove(request, film_id):
    cart = Cart(request)
    product = get_object_or_404(models.Film, id=film_id)

    cart.remove(product)

    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)

    return render(request, 'detail.html', {'cart': cart})


