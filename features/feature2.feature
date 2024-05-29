Feature: Login Feature

    @Test1
    Scenario Outline: 1.1 login with valid credentials
        Given I am on the "WebUrl" login page
        When User Enter "Username" on "Username" using "id" on "Login Page" Page
        And User Enter "Password" on "Password" using "id" on "Login Page" Page
        And User Click on "Login.Btn" using "id" on "Login Page" Page
        Examples:
            | username | password     |
            | Username | Password |
            | Invalid.Username | Invalid.Password |

    @Test2
    Scenario Outline: 1.2 login with valid credentials
        Given I am on the "WebUrl" login page
        When User Enter "Username" on "Username" using "id" on "Login Page" Page
        And User Enter "Password" on "Password" using "id" on "Login Page" Page
        And User Click on "Login.Btn" using "id" on "Login Page" Page
        Examples:
            | username | password     |
            | Username | Password |
            | Invalid.Username | Invalid.Password |

