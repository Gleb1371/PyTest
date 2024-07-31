def test_guest_should_see_add_to_basket_button(browser):
    # URL продукта для теста
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    
    # Ищем кнопку добавления в корзину
    add_to_basket_button = browser.find_element("css selector", ".btn-add-to-basket")
    assert add_to_basket_button is not None, "Add to basket button not found on the page"
