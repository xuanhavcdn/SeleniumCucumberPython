Feature: API testing demo
  Scenario: Test menu list
    Given The api is up and running
    When I get menu list
    Then The menu list should be response successfully with status code 200
    And The menu list should be response successfully with correct schema