from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK_BUTTON = (By.CLASS_NAME, "btn-group")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR,"input[name = registration-email]")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "input[name = registration-password1]")
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "input[name = registration-password2]")
    REGISTER_BUTTON_CONFIRM = (By.CSS_SELECTOR, "form#register_form > button[name='registration_submit']")

class ProductPageLocators():
    BUSKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")

    PRODUCT_NAME = (By.CSS_SELECTOR, '.product_main > h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR,"p[class = price_color]")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) strong')
    BASKET_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')

class BasketPageLocators():
    BASKET_PAGE_BUTTON =(By.CLASS_NAME, "btn-group")
    EMPTY_MESSAGE =(By.CSS_SELECTOR, "div.content div#content_inner > p > a")
    BACKET_ITEMS = (By.CSS_SELECTOR , "basket-items")

