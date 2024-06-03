Feature: Test Database Queries

Scenario: Run Custom SQL Query from Properties File and Save Results Without Parameters
    Given an empty table "users"
    When I insert a user with name "Ahad" and email "john@example.com"
    And I insert a user with name "Zuhair" and email "alice@example.com"

    Then User Run Query "query1" from "sql" File
    Then User Save Query Results as "NoParam1" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: " " from " " Page
    Then User Run Query "query3" from "sql" File
    Then User Save Query Results as "NoParamWithNoPropFileMultipleResults" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "Null" from "Null" Page
    Then User Run Query "query3" from "sql" File
    Then User Save Query Results as "NullParamWithNullPropFileMultipleResults" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "None" from "None" Page
    Then User Run Query "query3" from "sql" File
    Then User Save Query Results as "NoneParamWithNonePropFileMultipleResults" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: " " from "None" Page
    Then User Run Query "query3" from "sql" File
    Then User Save Query Results as "SPaceParamWithNonePropFileMultipleResults" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "None" from " " Page
    Then User Run Query "query3" from "sql" File
    Then User Save Query Results as "NoneParamWithNonePropFileMultipleResults" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: " " from " " Page
    Then User Run Query "query1" from "sql" File
    Then User Save Query Results as "NoParamNoPropFile" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "Ahad" from " " Page
    Then User Run Query "query" from "sql" File
    Then User Save Query Results as "OneParamNoPropFile" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "Ahad, john@example.com" from " " Page
    Then User Run Query "query2" from "sql" File
    Then User Save Query Results as "TwoParamNoPropFile" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "name2" from "./resources/test_data/login_page.properties" Page
    Then User Run Query "query" from "sql" File
    Then User Save Query Results as "OnePropWithPropFile" to "./resources/sql/results/sql_result.properties" File

    And User Enter Query Params: "name1, email" from "./resources/test_data/login_page.properties" Page
    Then User Run Query "query2" from "sql" File
    Then User Save Query Results as "TwoPropWithPropFile" to "./resources/sql/results/sql_result.properties" File

