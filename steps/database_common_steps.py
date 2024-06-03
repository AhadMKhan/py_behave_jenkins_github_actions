import logging

from behave import given, when, then

from Util_Factory.property_reader import PropertyReader
from Util_Factory.utility_factory import UtilityFactory
from base_factory.database_factory import DatabaseFactory


@given('an empty table "{table_name}"')
def step_given_empty_table(context, table_name):
    conn = DatabaseFactory.get_connection()
    DatabaseFactory.execute_query(conn, f"DROP TABLE IF EXISTS {table_name}")
    DatabaseFactory.execute_query(conn, f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT, email TEXT)")
    DatabaseFactory.close_connection(conn)


@when('I insert a user with name "{name}" and email "{email}"')
def step_when_insert_user(context, name, email):
    conn = DatabaseFactory.get_connection()
    DatabaseFactory.execute_query(conn, "INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    DatabaseFactory.close_connection(conn)


@when('User Enter Query Params: "{query_parameters}" from "{properties_file_path}" Page')
@then('User Enter Query Params: "{query_parameters}" from "{properties_file_path}" Page')
def step_store_parameters(context, query_parameters, properties_file_path):
    context.properties_file_path = properties_file_path
    context.query_parameters = DatabaseFactory.handle_query_parameters(query_parameters)
    logging.info(f"Query parameters: {context.query_parameters}")
    logging.info(f"Properties file path: {context.properties_file_path}")


@then('User Run Query "{sql_query}" from "{sql_query_file_path}" File')
def step_run_query_and_save(context, sql_query, sql_query_file_path):
    # Read the query from the properties file
    sql_query = PropertyReader.get_sql_query_property(sql_query, sql_query_file_path)
    logging.info(f"SQL query from file: {sql_query}")

    # Format the result saving key
    # sql_query_result_saving_key = UtilityFactory.make_property_name(sql_query_result_saving_key)

    # Process the query parameters if they exist
    query_parameters = getattr(context, 'query_parameters', None)
    properties_file_path = getattr(context, 'properties_file_path', None)
    sql_query = DatabaseFactory.set_query_parameter(sql_query, properties_file_path, query_parameters)
    logging.info(f"Formatted SQL query with parameters: {sql_query}")



    # Run the provided SQL query
    context.results = DatabaseFactory.run_query(sql_query)
    logging.info(f"Query results: {context.results}")


    # logging.info(context.results)
    #
    # # Save the results to a properties file with the specified path and main key
    # DatabaseFactory.save_results_to_properties(sql_query_result_saving_key, results, sql_query_result_saving_file_path)


@then('User Save Query Results as "{sql_query_result_saving_key}" to "{sql_query_result_saving_file_path}" File')
def step_run_query_and_save(context, sql_query_result_saving_key, sql_query_result_saving_file_path):
    sql_query_result_saving_key = UtilityFactory.make_property_name(sql_query_result_saving_key)


    # Save the results to a properties file with the specified path and main key
    DatabaseFactory.save_results_to_properties(sql_query_result_saving_key, context.results, sql_query_result_saving_file_path)
