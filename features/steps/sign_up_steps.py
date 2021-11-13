from behave import given, when, then
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class SignUpStepsTestCase(LiveServerTestCase):

    @given(u'I navigated to our online bank website')
    def step_impl(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        assert 'Online Bank' in self.browser.title, 'Expected {} but got {}'.format('Online Bank', self.browser.title)

    @when(u'I submit an application with valid details')
    def step_impl(self):
        # Click on the sign up button
        self.browser.find_element(By.ID, 'sign_up').click()

        # Check if we got to the sign up page
        assert 'Sign Up' in self.browser.title, 'Expected Sign Up but got {}'.format(self.browser.title)

        # Fill in the details

    @when(u'Select an account type')
    def step_impl(self):
        # Select an account type

        # Click the submit application button

        raise NotImplementedError(u'STEP: When Select an account type')

    @then(u'I am notified of my account status')
    def step_impl(self):
        raise NotImplementedError(u'STEP: Then I am notified of my account status')
