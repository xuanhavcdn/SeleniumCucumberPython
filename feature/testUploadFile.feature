Feature: Test upload file

  Scenario Outline: User able to upload the file "<file_storage_des>" successfully
    Given Access the URL
    When Submit the file "<file_storage>" MB
    And "<ticked_status>" check box accept term of service
    And Click on Submit button
    Then The "<message>" message is displayed correctly
    And Close browser
    Examples:
      | file_storage_des    | file_storage | ticked_status | message |
      | less than 196.45 MB | 196.45       | Yes           | success |
      | equal 196.45 MB     | 196.44       | Yes           | success |

  Scenario:  User able to view term of Service page successfully
    Given Access the URL
    When Click on Term of Service link
    Then The Term of Service link is displayed correctly
#   And The UI of Term of Service is displayed correctly
  # --The URL is not found so that cannot have expected result to validate
    And Close browser

  Scenario Outline: User unable to upload the file correctly with some condition: "<condition>"
    Given Access the URL
    When Submit the file "<file_storage>" MB
    And "<ticked_status>" check box accept term of service
    And Click on Submit button
    Then The "<message>" message is displayed correctly
    And Close browser
    Examples:
      | condition                       | file_storage | ticked_status | message |
      | File upload more than 196.45 MB | 196.46       | Yes           | error   |
      | Unticked term of service        | 196.45       | No            | error   |
      | Upload no file                  | 0            | Yes           | error   |


#  Scenario:  User unable to upload the file = 196.45 MB without ticked check box accept term of service
#    Given Access the URL
#    When Submit the file
#    And Ticked check box accept term of service
#    And Click on Submit button
#    Then The success message is displayed correctly
#    And Close browser
#
#  Scenario:  The error message is displayed when User click on Submit button without upload no file
#    Given Access the URL
#    When Submit the file
#    And Ticked check box accept term of service
#    And Click on Submit button
#    Then The success message is displayed correctly
#    And Close browser
#
#  Scenario:  User unable to submit the file with incorrect URL file
#    Given Access the URL
#    When Submit the file
#    And Ticked check box accept term of service
#    And Click on Submit button
#    Then The success message is displayed correctly
#    And Close browser
