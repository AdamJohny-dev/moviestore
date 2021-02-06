from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse
from django.test import LiveServerTestCase
from django.utils.encoding import force_bytes,force_text,DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode

class ClientBaseTestCase(LiveServerTestCase):

    """ Data fake to test """

    def setUp(self):

        """ Setting data """

        self.register_url=reverse('signup_client')
        self.login_url=reverse('login_client')
        self.user={
            'name':'name',
            'email':'testemail@gmail.com',
            'cpf':'cpf',
            'password':'password',
            'password2':'password',
            
        }
        self.user_short_password={
            'name':'name',
            'email':'testemail@gmail.com',
            'cpf':'111.222.333-44',
            'password':'tes',
            'password2':'tes',
            
        }
        self.user_unmatching_password={
            'name':'name',
            'email':'testemail@gmail.com',
            'cpf':'111.222.333-44',
            'password':'teslatt',
            'password2':'teslatto',
            
        }

        self.user_invalid_email={
            'name':'name',
            'email':'test.com',
            'cpf':'111.222.333-44',
            'password':'teslatt',
            'password2':'teslatto',
            
        }
        return super().setUp()
    
class RegisterTest(ClientBaseTestCase):

    """ Tests register feature """

    def test_can_view_page_correctly(self):

        """ Verify if rendered view is correct """

        response=self.client.get(self.register_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'clients/signup_client.html')

    def test_can_register_client(self):

        """ Verify if user can signup """

        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)    

    def test_cant_register_user_withshortpassword(self):

        """  Verify if length of password is greater than 4 """

        response=self.client.post(self.register_url,self.user_short_password,format='text/html')
        self.assertEqual(response.status_code,400)

    def test_cant_register_user_with_unmatching_passwords(self):

        """  Verify if passwords match"""
        
        response=self.client.post(self.register_url,self.user_unmatching_password,format='text/html')
        self.assertEqual(response.status_code,400)
        
    def test_cant_register_user_with_invalid_email(self):

        """  Verify if email is correct """
        
        response=self.client.post(self.register_url,self.user_invalid_email,format='text/html')
        self.assertEqual(response.status_code,400)

    def test_cant_register_user_with_taken_email(self):

        """  Verify if the given email exists on database """

        self.client.post(self.register_url,self.user,format='text/html')
        response=self.client.post(self.register_url,self.user,format='text/html')
        self.assertEqual(response.status_code,400)

class LoginTest(ClientBaseTestCase):

    """ Tests login feature """

    def test_can_access_page(self):

        """ Verify if rendered view is correct """

        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'clients/login_client.html')

    def test_login_success(self):

        """ Verify if login was done """
        
        self.client.post(self.register_url,self.user,format='text/html')
        user=User.objects.filter(email=self.user['email']).first()
        user.is_active=True
        user.save()
    
    def test_cantlogin_with_no_email(self):

        """ Verify the validator of email field """

        response= self.client.post(self.login_url,{'email':'','password':'test'},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_cantlogin_with_no_password(self):

        """ Verify the validator of password field """
        
        response= self.client.post(self.login_url,{'email':'test@test.com','password':''},format='text/html')
        self.assertEqual(response.status_code,401)


class LogoutTest(ClientBaseTestCase):

   """ Tests logout feature """

   def test_logout(self):

        """ Verify if user can logout"""
       
        self.client = Client()
        User.objects.create_user(username='Test', email='test@test.com', password='testing') 
        self.client.login(email='test@test.com', password="testing")
        response = self.client.get('/clients/logout_client')
        self.assertEqual(response.status_code, 302)