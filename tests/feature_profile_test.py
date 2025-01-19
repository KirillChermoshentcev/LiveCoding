from base.base_test import BaseTest
from conftest import driver
import random
import allure


@allure.feature("Profile Function")
class TestProfileFeature(BaseTest):

    @allure.title("Change Profile name")
    @allure.severity("Critical")
    def test_change_profile_name(self, driver):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.click_submit_button()
        self.dashboard.is_opened()
        self.dashboard.click_my_info_link()
        self.my_info_page.is_opened()
        self.my_info_page.change_name(f"Test {random.randint(1, 100)}")
        self.my_info_page.save_changes()
        self.my_info_page.is_changes_saved()
        self.my_info_page.make_screenshot("Success")

