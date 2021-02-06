from django.test import TestCase, RequestFactory
from django.urls import reverse
from apps.clients.views import signup

class ClientUrlsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_route_of_view_signup(self):

        """ Test the connection with view url"""

        url_signup = reverse('signup_client')
        self.assertEqual(url_signup, '/clients/signup_client')

    def test_status_code_of_view_signup(self):

        """ Test the status code of connection with view url """

        request = self.factory.get('/clients/signup_client')
        response = signup(request)

        self.assertEqual(response.status_code, 200)

