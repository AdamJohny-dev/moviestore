from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import  webdriver

class OwnerTestCase(LiveServerTestCase):
    
    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/CLIENTE/Pictures/application/chromedriver')

    def tearDown(self):
        self.browser.quit()
        
    
   

