from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class CardPage():
    # constructeur
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.but_checkout = '//a[@class="btn btn-lg btn-primary"]' # simple quote pour les string
        #self.link_first_item = '//img[@title="Canon EOS 5D"]'

    def Click_But_Checkout(self):
        c_but_checkout = self.driver.find_element(By.XPATH, self.but_checkout)
        c_but_checkout.click()

    #def Click_But_Checkout(self):
            #c_but_checkout = self.driver.find_element(By.XPATH, self.but_checkout)
            #c_but_checkout.click()