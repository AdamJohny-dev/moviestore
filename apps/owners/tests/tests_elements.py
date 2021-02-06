from django.test import LiveServerTestCase, RequestFactory
from django.urls import reverse
from selenium import  webdriver
from apps.owners.views import signup, dashboard

class OwnerElementsTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('C:/Users/CLIENTE/Pictures/application/chromedriver')
        self.factory = RequestFactory()
    
    def test_create_object_of_Client(self):
        home_page = self.browser.get(self.live_server_url+ '/owners/signup_owner')
        

        brand_element = self.browser.find_element_by_css_selector('.serialkey')
        self.assertEqual('Insert Key Serial', brand_element.text)
    
    def test_status_code_of_view_signup(self):

        """ Verify if the template rendered by the view is the correct """

        request = self.factory.get('/owners/signup_owner')
        with self.assertTemplateUsed('owners/signup_owner.html'):
            response = signup(request)
            self.assertEqual(response.status_code, 200)

