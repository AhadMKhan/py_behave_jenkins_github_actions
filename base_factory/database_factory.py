import os
import sqlite3
import xml.etree.ElementTree as ET
import logging

from Util_Factory.file_readers import FileReaders

logging.basicConfig(level=logging.INFO)


class DatabaseFactory:
    DATABASE_NAME = "test.db"
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_connection():
        return sqlite3.connect(DatabaseFactory.DATABASE_NAME)

    @staticmethod
    def close_connection(conn):
        conn.close()

    @staticmethod
    def execute_query(conn, query, params=None):
        try:
            with conn:
                conn.execute(query, params or [])
        except sqlite3.Error as e:
            DatabaseFactory.logger.error("Error executing query: %s", e)
            raise

    @staticmethod
    def fetch_all(conn, query, params=None):
        try:
            with conn:
                return conn.execute(query, params or []).fetchall()
        except sqlite3.Error as e:
            DatabaseFactory.logger.error("Error fetching results: %s", e)
            raise

    @staticmethod
    def save_results_to_xml(file_path, results, columns, num_rows=None):
        root = ET.Element("results")
        num_rows = num_rows or len(results)

        for idx, row in enumerate(results[:num_rows]):
            row_element = ET.SubElement(root, f"row_{idx + 1}")
            for value, column_name in zip(row, columns):
                column_element = ET.SubElement(row_element, column_name.strip())
                column_element.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(file_path)

    @staticmethod
    def save_results_to_properties(main_key, results, file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        existing_properties = {}
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                existing_properties = dict(line.strip().split('=') for line in f if '=' in line)

        with open(file_path, 'w') as f:
            for idx, row in enumerate(results):
                row_key = f"{main_key}.{idx + 1}" if len(results) > 1 else main_key
                row_str = ", ".join(map(str, row))
                existing_properties[row_key] = row_str

            for key, value in existing_properties.items():
                f.write(f"{key}={value}\n")

    @staticmethod
    def run_query(query):
        conn = DatabaseFactory.get_connection()
        try:
            return DatabaseFactory.fetch_all(conn, query)
        finally:
            DatabaseFactory.close_connection(conn)

    @staticmethod
    def handle_query_parameters(query_parameters):
        if query_parameters.lower() == "none":
            return None
        return query_parameters.split(', ')

    @staticmethod
    def set_query_parameter(sql_query, properties_file_path=None, *query_params):
        if not properties_file_path or properties_file_path.strip().lower() in {"none", "null", "", " "}:
            if query_params and isinstance(query_params[0], list):
                str_params = tuple(
                    param for sublist in query_params for param in sublist if isinstance(param, str) and param.strip())
            else:
                str_params = tuple(param for param in query_params if isinstance(param, str) and param.strip())
            # logging.info("String parameters: %s", str_params)
            if "null" in [param.lower() for param in str_params]:
                # logging.info("Null parameters provided, returning original query.")
                return sql_query
            if "none" in [param.lower() for param in str_params]:
                # logging.info("None parameters provided, returning original query.")
                return sql_query
            return sql_query % str_params if str_params else sql_query
        else:
            try:
                param_values = DatabaseFactory._fetch_param_values_from_properties(query_params, properties_file_path)
            except FileNotFoundError:
                logging.error("Properties file not found. Returning original query.")
                return sql_query
            if "null" in [param.lower() for param in param_values]:
                # logging.info("Null parameters provided, returning original query.")
                return sql_query
            if "none" in [param.lower() for param in param_values]:
                # logging.info("None parameters provided, returning original query.")
                return sql_query
            # logging.info("Parameter values from properties file: %s", param_values)
            return sql_query % tuple(param_values)

    @staticmethod
    def _fetch_param_values_from_properties(keys, properties_file_path):
        param_values = []
        for key in keys:
            if isinstance(key, (list, tuple)):
                param_values.extend(DatabaseFactory._fetch_param_values_from_properties(key, properties_file_path))
            elif key is not None:
                value = FileReaders.get_properties_property(key, properties_file_path)
                if value is None:
                    DatabaseFactory.logger.error("Property '%s' not found in the PROPERTIES data", key)
                    raise ValueError(f"Property '{key}' not found in the PROPERTIES data.")
                param_values.append(value)
        return param_values
