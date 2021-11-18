from behave import given, when, then
from django.contrib.staticfiles.testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class SignUpStepsTestCase(LiveServerTestCase):

    @given(u'I navigated to the most amazing online bank website ever')
    def step_impl(self):
        self.browser = webdriver.Chrome()
        self.browser.get('http://localhost:8000')
        title = self.browser.title
        assert 'Online Bank' in title, 'Expected {} but got {}'.format('Online Bank', title)

    @when(u'I apply with valid details for a "{account_type}" account')
    def step_impl(self, account_type):
        # Click on the sign up button
        self.browser.find_element(By.ID, 'sign_up').click()

        # Check if we got to the sign up page
        assert 'Sign Up' in self.browser.title, 'Expected Sign Up but got {}'.format(self.browser.title)

        # Fill in the details

        # Select account type
        time.sleep(1)

        # Submit the application
        self.browser.find_element(By.ID, 'submit').click()

    @then(u'I am notified of my "{expected_status}" account status')
    def step_impl(self, expected_status):
        status = self.browser.find_element(By.TAG_NAME, 'body').text
        assert 'Account ' + expected_status in status, 'Expected Account approved but got {}'.format(status)
