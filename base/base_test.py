import pytest
from conftest import *
from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard import DashboardPage
from pages.my_info_page import MyInfoPage


class BaseTest:

    data: Data

    login_page: LoginPage
    dashboard: DashboardPage
    my_info_page: MyInfoPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = self.driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard = DashboardPage(driver)
        request.cls.my_info_page = MyInfoPage(driver)
