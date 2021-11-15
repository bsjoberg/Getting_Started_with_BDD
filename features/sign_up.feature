Feature: Sign up for online bank account
  Scenario: Happy path sign up
    Given I navigated to our online bank website
    When I apply with valid details for a "checking" account
    Then I am notified of my "approved" account status