import time
import unittest

from selenium.webdriver.common.by import By
from selenium import webdriver

from html_elements.data import Data
from html_elements.page_elements import PageElements


class TestDouglasPage(unittest.TestCase, Data, PageElements):
    def setUp(self) -> None:
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get('https://www.douglas.ro/')
        self.driver.implicitly_wait(5)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_open_site(self):

        current_url = self.driver.current_url
        assert current_url == 'https://www.douglas.ro/', 'The curent URL not as expected. '
        print('The test is valid. ')

    def test_title(self):

        print(f'The current title is {self.driver.title}')
        assert 'Parfumerie DOUGLAS' in self.driver.title, f'The title {self.driver.title} does not contain "Parfumerie DOUGLAS". '
        print('The test is valid. ')

    def test_search_product(self):
        time.sleep(3)

        search_field = self.driver.find_element(*super().search_field)
        #search_field = self.driver.find_element(By.XPATH, '//input[@name="search" and @class="form-control header-search-input"]')
        search_field.send_keys('gucci')
        time.sleep(3)

        search_button = self.driver.find_element(*super().search_button)
        search_button.click()
        time.sleep(3)
        print('The current URL is: ', self.driver.current_url)
        assert self.driver.current_url == "https://www.douglas.ro/search?search=gucci", 'The URL is not as expected. '

        products = self.driver.find_elements(By.CLASS_NAME, 'e-product-brand')
        nr_products = len(products)
        print('Products nr. = ', nr_products)
        assert nr_products >= 10, 'Products number lower than 10.'
        print('The test is valid ')

    def test_lowest_price_product(self):
        self.test_search_product()
        products = self.driver.find_elements(By.CLASS_NAME, 'product-price')
        lowest_price = float('inf')
        prices = []

        for product in products:
            price = product.text.replace(' RON', '').replace(',', '.')
            prices.append(price)
            #print(prices)

        for new_price in prices:
            if (' 'in new_price):
                new_price = new_price[new_price.index(' ') +1:]
            if float(new_price) < float(lowest_price):
                lowest_price = float(new_price)

        print(f"The lowest price is: {lowest_price}")
        assert lowest_price <= 175, 'The lowest price is not as expected. '
        print('The test is valid. ')

    def test_valid_login(self):

        self.driver.get(super().log_in_page_url)
        self.driver.implicitly_wait(5)

        email = self.driver.find_element(*super().email_field)
        email.send_keys(super().valid_email)
        time.sleep(3)

        passwword = self.driver.find_element(*super().password_field)
        passwword.send_keys(super().valid_password)
        time.sleep(3)

        login_button = self.driver.find_element(*super().login_button)
        login_button.click()
        time.sleep(3)

        actual_url = self.driver.current_url
        assert actual_url == super().logged_in_page_url, 'The URL is not as expected. '
        print(actual_url)
        print('The test is valid. ')

    def test_invalid_email(self):

        self.driver.get(super().log_in_page_url)
        self.driver.implicitly_wait(5)

        email = self.driver.find_element(*super().email_field)
        email.send_keys(super().valid_email + '1')
        time.sleep(3)

        passwword = self.driver.find_element(*super().password_field)
        passwword.send_keys(super().valid_password)
        time.sleep(3)

        login_button = self.driver.find_element(*super().login_button)
        login_button.click()
        time.sleep(3)

        error_message = self.driver.find_element(*super().error_label)
        assert error_message.text == super().error_login_message, 'The login error message not as expected. '
        print(error_message.text)
        print('The test is valid. ')

    def test_invalid_password(self):

        self.driver.get(super().log_in_page_url)
        self.driver.implicitly_wait(5)

        email = self.driver.find_element(*super().email_field)
        email.send_keys(super().valid_email)
        time.sleep(3)

        passwword = self.driver.find_element(*super().password_field)
        passwword.send_keys(super().valid_password + '1')
        time.sleep(3)

        login_button = self.driver.find_element(*super().login_button)
        login_button.click()
        time.sleep(3)

        error_message = self.driver.find_element(*super().error_label)
        assert error_message.text == super().error_login_message, 'The login error message not as expected. '
        print(error_message.text)
        print('The test is valid. ')

    def test_logout(self):
        self.driver.get(super().log_in_page_url)
        self.driver.implicitly_wait(5)

        email = self.driver.find_element(*super().email_field)
        email.send_keys(super().valid_email)
        time.sleep(3)

        passwword = self.driver.find_element(*super().password_field)
        passwword.send_keys(super().valid_password)
        time.sleep(3)

        login_button = self.driver.find_element(*super().login_button)
        login_button.click()
        time.sleep(3)

        logout_button = self.driver.find_element(*super().logout_button)
        logout_button.click()
        time.sleep(2)

        logout_message = self.driver.find_element(*super().logout_message_label)
        assert logout_message.text == super().logout_message_ok, 'The logout message not as expected. '
        print(logout_message.text)
        print('The test is valid')

    def test_add_product(self):
        time.sleep(1)

        search_field = self.driver.find_element(*super().search_field)
        search_field.send_keys('it cosmetics')
        time.sleep(2)

        search_button = self.driver.find_element(*super().search_button)
        search_button.click()
        time.sleep(3)

        item = self.driver.find_element(*super().it_cosmetics)
        item.click()
        time.sleep(2)

        add = self.driver.find_element(*super().add_button)
        add.click()
        time.sleep(2)

        message = self.driver.find_element(*super().add_label)
        assert message.text == super().added_item, 'The added item message is not as expected. '
        print(message.text)
        print('The test is valid. ')

    def test_wish_list(self):
        self.test_valid_login()

        wish_list = self.driver.find_element(*super().wish_list)
        wish_list.click()
        time.sleep(1)

        wish_list_button = self.driver.find_element(*super().wish_list_button)
        wish_list_button.click()
        time.sleep(2)

        new_list = self.driver.find_element(*super().new_list)
        new_list.send_keys('lista')
        time.sleep(1)
        new_list_save = self.driver.find_element(*super().new_list_button)
        new_list_save.click()
        time.sleep(1)

        error_message = self.driver.find_element(*super().new_list_error_label)
        assert error_message.text == super().list_message_error, 'The error message not as expected. '
        #assert error_message.is_displayed() == True, 'The error message not as expected. '
        print(error_message.text)
        print('The test is valid')
