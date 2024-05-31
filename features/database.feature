Feature: Test Database Queries

Scenario: Run Custom SQL Query from Properties File and Save Results Without Parameters
    Given an empty table "users"
    When I insert a user with name "Ahad" and email "john@example.com"
    And I insert a user with name "Jazlan" and email "alice@example.com"
    Then User Run Query "query1" from "sql" and save the results to "./resources/sql/results/sql_result.properties" with key "NoParam1"

    And User Enter Query Params: " " from " " Page
    Then User Run Query "query1" from "sql" and save the results to "./resources/sql/results/sql_result.properties" with key "NoParamWithPropFile"

    And User Enter Query Params: "Ahad" from " " Page
    Then User Run Query "query" from "sql" and save the results to "./resources/sql/results/sql_result.properties" with key "SingParamWithoutPropFile"

    And User Enter Query Params: "Ahad, john@example.com" from " " Page
    Then User Run Query "query2" from "sql" and save the results to "./resources/sql/results/sql_result.properties" with key "MultiParamWithoutPropFile"

    And User Enter Query Params: "name2" from "./resources/test_data/login_page.properties" Page
    Then User Run Query "query" from "sql" and save the results to "./resources/sql/results/sql_result.properties" with key "SingParamWithPropFile"

    And User Enter Query Params: "name1, email" from "./resources/test_data/login_page.properties" Page
    Then User Run Query "query2" from "sql" and save the results to "./resources/sql/results/sql_result.properties" with key "MultiParamWithPropFile"
