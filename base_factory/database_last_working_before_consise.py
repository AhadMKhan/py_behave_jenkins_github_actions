from Util_Factory.file_readers import FileReaders
from base_factory.database_factory import DatabaseFactory

sql_query1 = "SELECT * FROM users WHERE name = '%s' AND email = '%s'"
query2 = "SELECT name FROM users where name='%s'"
query3 = "SELECT name FROM users where name='Ahad'"

properties_proptey = ['Ahad']
properties_proptey1 = ['Ahad', 'john@example.com']
properties_proptey12 = ['name1']
properties_proptey13 = ['name1', 'email']

properties_file_path = "../resources/test_data/login_page.properties"

case1 = "Case 1: None Direct parameters without properties file: \n"
print(case1 + DatabaseFactory.set_query_parameter(query2, None, properties_proptey) + "\n")

case1 = "Case 1: "" Direct parameters without properties file: \n"
print(case1 + DatabaseFactory.set_query_parameter(sql_query1, "", properties_proptey1) + "\n")

case1 = "Case 1: Null Direct parameters without properties file: \n"
print(case1 + DatabaseFactory.set_query_parameter(sql_query1, "Null", "Ahad", "john@example.com") + "\n")

case1 = "Case 1: Space Direct parameters without properties file: \n"
print(case1 + DatabaseFactory.set_query_parameter(sql_query1, " ", "Ahad", "john@example.com") + "\n")

case2 = "Case 2: One proptery Parameters with properties file: \n"
print(case2 + DatabaseFactory.set_query_parameter(query2, properties_file_path, properties_proptey12) + "\n")

case2 = "Case 2: Two Parameters with properties file: \n"
print(case2 + DatabaseFactory.set_query_parameter(sql_query1, properties_file_path, properties_proptey13) + "\n")

# Object created but nothing passed
case3 = "Case 3: None No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, None, None) + "\n")

# Object created but nothing passed
case3 = "Case 3: None as string No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, "None", "None") + "\n")

case3 = "Case 3: SMall None as string No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, "none", "none") + "\n")

case3 = "Case 3: "" No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, "", "") + "\n")

case3 = "Case 3: " " No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, " ", " ") + "\n")

# Nothing passed nor object created
case4 = "Case 4: Not Provided No parameters or properties: \n"
print(case4 + DatabaseFactory.set_query_parameter(query3) + "\n")

case3 = "Case 3: Null as string No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, "Null", "Null") + "\n")

case3 = "Case 3: SMall Null as string No parameters or properties: \n"
print(case3 + DatabaseFactory.set_query_parameter(query3, "null", "null") + "\n")

# @staticmethod
# def set_query_parameter(sql_query, properties_file_path=None, *query_params):
#     if not properties_file_path or properties_file_path.strip().lower() in {"none","null", "", " "}:
#         if query_params and isinstance(query_params[0], list):
#             str_params = tuple(
#                 param for sublist in query_params for param in sublist if isinstance(param, str) and param.strip())
#         else:
#             str_params = tuple(param for param in query_params if isinstance(param, str) and param.strip())
#         # logging.info("String parameters: %s", str_params)
#         if "Null" in str_params:
#             # logging.info("Null parameters provided, returning original query.")
#             return sql_query
#         if "None" in str_params:
#             # logging.info("None parameters provided, returning original query.")
#             return sql_query
#         return sql_query % str_params if str_params else sql_query
#     else:
#         try:
#             param_values = DatabaseFactory._fetch_param_values_from_properties(query_params, properties_file_path)
#         except FileNotFoundError:
#             logging.error("Properties file not found. Returning original query.")
#             return sql_query
#         if "Null" in param_values:
#             # logging.info("Null parameters provided, returning original query.")
#             return sql_query
#         if "None" in param_values:
#             # logging.info("None parameters provided, returning original query.")
#             return sql_query
#         # logging.info("Parameter values from properties file: %s", param_values)
#         return sql_query % tuple(param_values)

# #####last working code before make more consises
