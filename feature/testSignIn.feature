Feature: Test sign in feature
  Scenario Outline: Verify user able to login success with correct username and password
    Given Access the React URL
    When Click on Sign in option button
    And Input email as "<email>" and password as "<password>"
    And Click on Sign up button
    Then Home screen is display correctly with correct username
    And Close browser
    Examples:
      | email   | password |
      | <email> | Hacao    |