Feature: Logged Feature

    @Test1
    Scenario: 2.1 with valid credentials
        Given I am on the "WebUrl" login page
        When User Enter "Username" on "Username" using "id" on "Login Page" Page
        And User Enter "Password" on "Password" using "id" on "Login Page" Page
        And User Click on "Login.Btn" using "id" on "Login Page" Page
        And User Assert "Products" on "Homepage.Heading" using "xpath" on "Login Page" Page
#
#        Examples:
#            | username | password     |
#            | Username | Password |
#            | Invalid.Username | Invalid.Password |

    @Test2
    Scenario Outline: 2.2 login with valid credentials
        Given I am on the "WebUrl" login page
        When User Enter "Username" on "Username" using "id" on "Login Page" Page
        And User Enter "Password" on "Password" using "id" on "Login Page" Page
        And User Click on "Login.Btn" using "id" on "Login Page" Page
        Examples:
            | username | password     |
            | Username | Password |
            | Invalid.Username | Invalid.Password |

