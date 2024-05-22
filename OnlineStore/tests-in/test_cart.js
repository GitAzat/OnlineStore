import { Selector } from 'testcafe';

fixture`Adding Item to Cart`
    .page`http://127.0.0.1:8000`; // замените на URL вашего сайта

test('Add Item to Cart', async t => {
    // Нажимаем кнопку "Добавить в корзину"
    await t.click(Selector('a').withText('Добавить в корзину'));

    // Проверяем, что корзина не пуста после добавления товара
    await t.expect(Selector('.cart-table').exists).ok();

    // Проверяем, что добавленный товар отображается в корзине
    await t.expect(Selector('.cart-item-title').withText('Тестовый товар').exists).ok();
});
