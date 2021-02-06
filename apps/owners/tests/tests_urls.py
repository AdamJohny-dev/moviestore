from django.test import TestCase, RequestFactory
from django.urls import reverse
from apps.owners.views import signup

class OwnerUrlsTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_route_of_view_signup(self):

        """ Test the connection with view url"""

        url_signup = reverse('signup_owner')
        self.assertEqual(url_signup, '/owners/signup_owner')

    def test_status_code_of_view_signup(self):

        """ Test the status code of connection with view url """

        request = self.factory.get('/owners/signup_owner')
        response = signup(request)

        self.assertEqual(response.status_code, 200)

