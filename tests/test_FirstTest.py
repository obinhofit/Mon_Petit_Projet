import sys
import os

import pytest
from time import sleep


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))  # .. on remontepip

from helpers.BaseTest import BaseTest
from pages.HomePage import HomePage
from pageFragments.HeaderPageFragment import HeaderPageFragment
from pages.ProductListPage import ProductListPage
from pages.ProductPage import ProductPage
from pageFragments.CardPopUpPage import CardPopUpPage
from pages.CardPage import CardPage
from pages.CheckoutPage import CheckoutPage

class Test_FirstTest(BaseTest):  # héritage

    @pytest.mark.test_MyFirstTest
    def test_MyFirstTest(self):
        print("My First Test")
        self.open_application()

        home = HomePage(self.driver)
        home.is_page_visible("Your Store")

        header = HeaderPageFragment(self.driver)
        header.select_menu()
        header.select_subMenu()


        productliste = ProductListPage(self.driver)
        productliste.select_in_stock()
        sleep(3)
        productliste.clickOn_link_first_item()


        buttonCard = ProductPage(self.driver)
        buttonCard.click_but_add_card()
        sleep(3)

        butviewCard = CardPopUpPage(self.driver)
        butviewCard.click_but_view_card()
        sleep(3)


        butCardPage = CardPage(self.driver)
        butCardPage.Click_But_Checkout()
        sleep(3)

        Guestcheckout = CheckoutPage (self.driver)
        Guestcheckout.Select_Guest_Checkout()
        sleep(3)