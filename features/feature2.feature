Feature: Login Feature

    @Test1
    Scenario Outline: 1.1 login with valid credentials
        Given I am on the login page
        When I enter username "<username>" and password "<password>"
        And I click the login button
        Examples:
            | username      | password     |
            | standard_user | secret_sauce |

    @Test2
    Scenario Outline: 1.2 login with valid credentials
        Given I am on the login page
        When I enter username "<username>" and password "<password>"
        And I click the login button
        Examples:
            | username      | password     |
            | standard_user | secret_sauce |
            | test          | test         |

