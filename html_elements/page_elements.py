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
    because_you = (By.XPATH, '//div[@data-elio-ff-parent-product-id="94bcd8dccc0d4d40a5f4f596ce31ec31"]')
    add_button = (By.XPATH, '//button[@class="btn btn-block btn-buy e-btn-buy"]')
    add_label = (By.XPATH, '//div[@role="alert" and @class="alert alert-success alert-has-icon"]')
