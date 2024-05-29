Feature: API Testing with Behave

  Scenario: Verify status code of a GET request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    When I send a "GET" request to the endpoint
    Then the status code should be 200

  Scenario: Verify status code of a POST request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts"
    And I have the payload from JSON file "post_request"
    When I send a "POST" request to the endpoint
    Then the status code should be 201

  Scenario: Verify status code of a PUT request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    And I have the payload from JSON file "put_request"
    When I send a "PUT" request to the endpoint
    Then the status code should be 200

  Scenario: Verify status code of a DELETE request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    When I send a "DELETE" request to the endpoint
    Then the status code should be 200

  Scenario: Verify status code of a PATCH request
    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
    And I have the payload from JSON file "patch_request"
    When I send a "PATCH" request to the endpoint
    Then the status code should be 200

#Feature: API Testing with Behave
#
#  Scenario: Verify status code of a GET request
#    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
#    When I send a "GET" request to the endpoint
#    Then the status code should be 200
#
#  Scenario: Verify status code of a POST request
#    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts"
#    And I have the payload
#      """
#      {
#        "title": "foo",
#        "body": "bar",
#        "userId": 1
#      }
#      """
#    When I send a "POST" request to the endpoint
#    Then the status code should be 201
#
#  Scenario: Verify status code of a PUT request
#    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
#    And I have the payload
#      """
#      {
#        "id": 1,
#        "title": "foo",
#        "body": "bar",
#        "userId": 1
#      }
#      """
#    When I send a "PUT" request to the endpoint
#    Then the status code should be 200
#
#  Scenario: Verify status code of a DELETE request
#    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
#    When I send a "DELETE" request to the endpoint
#    Then the status code should be 200
#
#  Scenario: Verify status code of a PATCH request
#    Given I have the API endpoint "https://jsonplaceholder.typicode.com/posts/1"
#    And I have the payload
#      """
#      {
#        "title": "foo patched"
#      }
#      """
#    When I send a "PATCH" request to the endpoint
#    Then the status code should be 200
