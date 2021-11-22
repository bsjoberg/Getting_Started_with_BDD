import unittest
import xmlrunner
from django.test import TestCase


class HelloWorldPageTest(TestCase):

    def test_uses_hello_world_template(self):
        response = self.client.get('/hello_world/')
        self.assertTemplateUsed(response, 'hello_world.html')


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')


class SignUpTest(TestCase):

    def test_uses_sign_up_template(self):
        response = self.client.get('/sign_up/')
        self.assertTemplateUsed(response, 'sign_up.html')

    def test_uses_application_status_template(self):
        response = self.client.get('/application_status/')
        self.assertTemplateUsed(response, 'application_status.html')
