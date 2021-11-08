from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BUSKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p[class = price_color]")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

