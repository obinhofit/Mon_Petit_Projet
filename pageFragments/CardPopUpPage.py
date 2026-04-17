from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class CardPopUpPage():
    # constructeur
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.but_view_card = '//a[@class="btn btn-primary btn-block"]' # simple quote pour les string
        #self.link_first_item = '//img[@title="Canon EOS 5D"]'


    def click_but_view_card(self):
        c_but_view_card = self.driver.find_element(By.XPATH, self.but_view_card)
        c_but_view_card .click()

        print("ALLEZ L'OL")


    #def clickOn_link_first_item(self):
        #c_link_first_item = self.driver.find_element(By.XPATH, self.link_first_item)
        #c_link_first_item.click()