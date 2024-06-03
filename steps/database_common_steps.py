import logging

from behave import given, when, then  # pylint: disable=no-name-in-module

from Util_Factory.property_reader import PropertyReader
from Util_Factory.utility_factory import UtilityFactory
from base_factory.database_factory import DatabaseFactory


@given('an empty table "{table_name}"')
def step_given_empty_table(context, table_name):  # pylint: disable=W0613
    conn = DatabaseFactory.get_connection()
    DatabaseFactory.execute_query(conn, f"DROP TABLE IF EXISTS {table_name}")
    DatabaseFactory.execute_query(
        conn,
        f"CREATE TABLE {table_name} (id INTEGER PRIMARY KEY, name TEXT, email TEXT)",
    )
    DatabaseFactory.close_connection(conn)


@when('I insert a user with name "{name}" and email "{email}"')
def step_when_insert_user(context, name, email):  # pylint: disable=W0613
    conn = DatabaseFactory.get_connection()
    DatabaseFactory.execute_query(
        conn, "INSERT INTO users (name, email) VALUES (?, ?)", (name, email)
    )
    DatabaseFactory.close_connection(conn)


@when(
    'User Enter Query Params: "{query_parameters}" from "{properties_file_path}" Page'
)
@then(
    'User Enter Query Params: "{query_parameters}" from "{properties_file_path}" Page'
)
def step_store_parameters(context, query_parameters, properties_file_path):
    context.properties_file_path = properties_file_path
    context.query_parameters = DatabaseFactory.handle_query_parameters(query_parameters)
    logging.info("Query parameters: %s", context.query_parameters)
    logging.info("Properties file path: %s", context.properties_file_path)


@then('User Run Query "{sql_query}" from "{sql_query_file_path}" File')
def run_select_query(context, sql_query, sql_query_file_path):
    # Read the query from the properties file
    sql_query = PropertyReader.get_sql_query_property(sql_query, sql_query_file_path)
    logging.info("SQL query from file: %s", sql_query)

    # Process the query parameters if they exist
    query_parameters = getattr(context, "query_parameters", None)
    properties_file_path = getattr(context, "properties_file_path", None)
    sql_query = DatabaseFactory.set_query_parameter(
        sql_query, properties_file_path, query_parameters
    )
    logging.info("Formatted SQL query with parameters: %s", sql_query)

    # Run the provided SQL query
    context.results = DatabaseFactory.run_query(sql_query)
    logging.info("Query results: %s", context.results)


@then(
    'User Save Query Results as "{sql_query_result_saving_key}" to "{sql_query_result_saving_file_path}" File'
)
def save_query_results(
    context, sql_query_result_saving_key, sql_query_result_saving_file_path
):
    sql_query_result_saving_key = UtilityFactory.make_property_name(
        sql_query_result_saving_key
    )

    DatabaseFactory.save_results_to_properties(
        sql_query_result_saving_key, context.results, sql_query_result_saving_file_path
    )
