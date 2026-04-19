from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class CheckoutPage():

    # --/  Constructeur
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.guest_checkout = '//Label[contains(text(), "Guest Checkout")]' # simple quote pour les string
        #self.link_first_item = '//img[@title="Canon EOS 5D"]'

    # --/ Méthode
    def Select_Guest_Checkout(self):
        c_guest_checkout = self.driver.find_element(By.XPATH, self.guest_checkout)
        c_guest_checkout.click()

    #def Click_But_Checkout(self):
            #c_but_checkout = self.driver.find_element(By.XPATH, self.but_checkout)
            #c_but_checkout.click()
