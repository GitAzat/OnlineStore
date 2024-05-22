from django.test import TestCase
from django.urls import reverse
from store.models import Item

class AddToCartViewTest(TestCase):
    def setUp(self):
        # Создаем тестовый товар
        self.item = Item.objects.create(
            title='Тестовый товар',
            description='Описание тестового товара',
            slug='testovyy-tovar',
            price=50.00,
            old_price=40.00,
            is_available=True,
        )

    def test_add_to_cart_view(self):
        # Отправляем POST-запрос для добавления товара в корзину
        response = self.client.post(reverse('cart:add_to_cart', kwargs={'item_slug': self.item.slug}))

        # Проверяем, что запрос завершился успешно
        self.assertEqual(response.status_code, 302)  # Ожидаем редирект, так как товар добавлен в корзину

        # Здесь можно добавить дополнительные проверки, например, убедиться, что товар добавлен в корзину

