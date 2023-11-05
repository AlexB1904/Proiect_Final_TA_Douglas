from selenium.webdriver.common.by import By


class PageElements:
    search_field = (By.XPATH, '//input[@name="search" and @class="form-control header-search-input"]')
    search_button = (By.XPATH, '//button[@type="submit" and @class="btn header-search-btn"]')
    email_field = (By.XPATH, '//input[@id="loginMail"]')
    password_field = (By.XPATH, '//input[@id="loginpasswordfield"]')
    login_button = (By.XPATH, '//div[@class="login-submit"]/button[@type="submit" and @class="btn btn-primary"]')
    logout_button = (By.XPATH, '//main/div/div/div/div/div/div/div/div/a[@class="btn btn-link account-aside-btn" and "account/logout"]')
    error_label = (By.XPATH, '//div[@role="alert"]')
    logout_message_label = (By.XPATH, '//div[@class = "alert-content"]')
    it_cosmetics = (By.XPATH, '//div[@data-elio-ff-parent-product-id="16642b6bb3f446dca29cf157e78c1632"]')
    add_button = (By.XPATH, '//button[@class="btn btn-block btn-buy e-btn-buy"]')
    add_label = (By.XPATH, '//div[@role="alert" and @class="alert alert-success alert-has-icon"]')
    wish_list = (By.XPATH, '//a[@class="btn header-wishlist-btn header-actions-btn"]')
    wish_list_button = (By.XPATH, '//button[@class="btn btn-primary" and @data-toggle="modal"]' )
    new_list = (By.XPATH, '//input[@id="wishlistNewName"]')
    new_list_button = (By.XPATH, '//button[@class="btn btn-primary wl-save-button"]')
    new_list_error_label = (By.XPATH, '//div[@class="alert alert-danger alert-has-icon"]//div//div[@class="alert-content"]')





