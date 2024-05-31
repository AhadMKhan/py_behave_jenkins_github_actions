# def set_query_parameter(sql_query, properties_file_path=None, *query_params):
#     # If properties_file_path is None, empty, "null", or consists only of whitespace characters,
#     # treat query_params as the values directly
#     if not properties_file_path or properties_file_path.strip().lower() in {"null", "", " "}:
#         if query_params and any(
#                 isinstance(param, str) and param.strip().lower() not in {"null", ""} for param in query_params):
#             return sql_query % tuple(param for param in query_params if
#                                      isinstance(param, str) and param.strip().lower() not in {"null", ""})
#         else:
#             return sql_query
#     else:
#         # If properties_file_path is valid, fetch the parameter values from the properties file
#         if query_params:
#             query_parameter_values = []
#             for key in query_params:
#                 if key is not None:
#                     value = FileReaders.get_properties_properties(properties_file_path, key)
#                     if value is None:
#                         raise ValueError(f"Property '{key}' not found in the PROPERTIES data.")
#                     query_parameter_values.append(value)
#
#             # Return the formatted query string with parameters from properties file
#             return sql_query % tuple(query_parameter_values)
#         else:
#             return sql_query

from Util_Factory.file_readers import FileReaders

def set_query_parameter(sql_query, properties_file_path=None, *query_params):
    # If properties_file_path is None, empty, "null", or consists only of whitespace characters,
    # treat query_params as the values directly
    if not properties_file_path or properties_file_path.strip().lower() in {"null", "", " "}:
        if query_params and any(
                isinstance(param, str) and param.strip().lower() not in {"null", ""} for param in query_params):
            return sql_query % tuple(param for param in query_params if
                                     isinstance(param, str) and param.strip().lower() not in {"null", ""})
        else:
            return sql_query
    # else:
    # # If properties_file_path is valid, fetch the parameter values from the properties file
    #     query_parameter_values = []
    #     for key in query_params:
    #         if isinstance(key, (list, tuple)):
    #             query_parameter_values.extend(key)  # Unpack the list or tuple and add to the list
    #         else:
    #             if key is not None:
    #                 value = FileReaders.get_properties_property(properties_file_path, key)
    #                 if value is None:
    #                     raise ValueError(f"Property '{key}' not found in the PROPERTIES data.")
    #                 query_parameter_values.append(value)
    #
    #     # Return the formatted query string with parameters from properties file
    #     return sql_query % tuple(query_parameter_values)

    else:
        # If properties_file_path is valid, fetch the parameter values from the properties file
        query_parameter_values = []
        for key in query_params:
            if isinstance(key, (list, tuple)):
                for k in key:
                    value = FileReaders.get_properties_property(k, properties_file_path)
                    if value is None:
                        raise ValueError(f"Property '{k}' not found in the PROPERTIES data.")
                    query_parameter_values.append(value)
            else:
                if key is not None:
                    value = FileReaders.get_properties_property(key, properties_file_path)
                    if value is None:
                        raise ValueError(f"Property '{key}' not found in the PROPERTIES data.")
                    query_parameter_values.append(value)

        # Return the formatted query string with parameters from properties file
        return sql_query % tuple(query_parameter_values)



sql_query1 = "SELECT * FROM users WHERE name = '%s' AND email = '%s'"
query2 = "SELECT name FROM users where name='%s'"
query3 = "SELECT name FROM users where name='Ahad'"
properties_proptey =['name1']
properties_proptey1 =['name1', 'email']

properties_file_path = "../resources/test_data/login_page.properties"

case1 = "Case 1: None Direct parameters without properties file: \n"
print(case1+set_query_parameter(sql_query1, None, "Ahad", "john@example.com")+"\n")

case1 = "Case 1: "" Direct parameters without properties file: \n"
print(case1+set_query_parameter(sql_query1, "", "Ahad", "john@example.com")+"\n")

case1 = "Case 1: Null Direct parameters without properties file: \n"
print(case1+set_query_parameter(sql_query1, "Null", "Ahad", "john@example.com")+"\n")

case1 = "Case 1: Space Direct parameters without properties file: \n"
print(case1+set_query_parameter(sql_query1, " ", "Ahad", "john@example.com")+"\n")


case2 = "Case 2: One proptery Parameters with properties file: \n"
print(case2+set_query_parameter(sql_query1, properties_file_path, properties_proptey1)+"\n")

case2 = "Case 2: Two Parameters with properties file: \n"
print(case2+set_query_parameter(query2, properties_file_path, properties_proptey)+"\n")
#Nothing passed nor object created
case4 = "Case 4: Not Provided No parameters or properties: \n"
print(case4+set_query_parameter(query3)+"\n")

#Object created but nothing passed
case3 = "Case 3: None No parameters or properties: \n"
print(case3+set_query_parameter(query3, None, None)+"\n")

case3 = "Case 3: Null No parameters or properties: \n"
print(case3+set_query_parameter(query3, "Null", "Null")+"\n")

case3 = "Case 3: "" No parameters or properties: \n"
print(case3+set_query_parameter(query3, "", "")+"\n")

case3 = "Case 3: " " No parameters or properties: \n"
print(case3+set_query_parameter(query3, " ", " ")+"\n")