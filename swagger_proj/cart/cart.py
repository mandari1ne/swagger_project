from decimal import Decimal
from django.conf import settings
# from swagger_proj.films import models
from films import models

class Cart:

    def __init__(self, request):

        self.session = request.session # текущая сессия

        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            # если корзина пустая
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart # уже в поле класса корзины передается значение корзины


    def add(self, product, quantity=1, update_quantity=False):

        product_id = str(product.id)

        # цена преобразовывается из десятичного в строку для СЕРИАЛИЗАЦИИ

        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)
            }

        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity

        self.save() # СОХРАНЕНИЕ ИЗМЕНЕНИЙ В СЕССИИ


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart # обновление корзины для текущей сессии

        self.session.modified = True
        # с помощью этого мы говорим "self.session modified и должна быть сохранена"


    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]

            self.save()


    # с помощью магического метода создаем итератор по элементам корзины
    def __iter__(self):
        films_id = self.cart.keys()

        films = models.Film.objects.filter(id__in=films_id)

        for film in films:
            self.cart[str(film.id)]['product'] = film

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])

            item['total_price'] = item['quantity'] * item['price']

            yield item


    # общее количество товаров для каждого продукта в нашей корзине
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    # удаление корзины из сессии
    def clear(self):
        del self.session[settings.CART_SESSION_ID]

        self.session.modified = True
