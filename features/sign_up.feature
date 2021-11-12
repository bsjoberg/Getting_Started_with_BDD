Feature: Sign up for online bank account
  Scenario: Happy path sign up
    Given I navigated to our online bank website
    When I submit an application with valid details
    And Select an account type
    Then I am notified of my account status