from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class ProductListPage():
    # constructeur
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.lbl_filter_availability = '//label[@for="mz-fss-0--1"]' # simple quote pour les string
        self.link_first_item = '(//*[@class="carousel-item active"]/*[@class="lazy-load"])[3]'


    def select_in_stock(self):
        c_lbl_filter_availability = self.driver.find_element(By.XPATH, self.lbl_filter_availability)
        c_lbl_filter_availability.click()


    def clickOn_link_first_item(self):
        c_link_first_item = self.driver.find_element(By.XPATH, self.link_first_item)
        c_link_first_item.click()