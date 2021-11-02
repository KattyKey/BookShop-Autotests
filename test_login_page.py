from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/accounts/login/"
link_wrong_test = "http://selenium1py.pythonanywhere.com/"

def test_guest_should_be_login(browser):
    page = LoginPage(browser, link_wrong_test)
    page.open()
    page.should_be_login_url()

def test_guest_should_be_login_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_guest_should_be_register_form(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()

def test_guest_should_be_login_page(browser):
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
