Feature: Test sign up

  Scenario Outline: User able to sign up successfully
    Given Access the React URL
    When Click on Sign up option
    And Input username as "<username>" and email as "<email>" and Password as "<password>"
    And Click on Sign up button
    Then Home screen is displayed correctly with correct username
    And Close browser
    Examples:
      | username   | password | email   |
      | <username> | Ha@cao   | <email> |