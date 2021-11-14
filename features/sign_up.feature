Feature: Sign up for online bank account
  Scenario: Happy path sign up
    Given I navigated to our online bank website
    When I submit an application with valid details for a "checking" account
    Then I am notified of my account status