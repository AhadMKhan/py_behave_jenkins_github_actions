import json
import xml.etree.ElementTree as ET
import yaml
import logging

# Constants
JSON_TYPE = 'json'
XML_TYPE = 'xml'
YAML_TYPE = 'yaml'
PROPERTIES_TYPE = 'properties'


class FileReaders:
    @staticmethod
    def read_file(file_path, file_type):
        try:
            if file_type == JSON_TYPE:
                with open(file_path, 'r') as file:
                    return json.load(file)
            elif file_type == XML_TYPE:
                tree = ET.parse(file_path)
                return tree.getroot()
            elif file_type == YAML_TYPE:
                with open(file_path, 'r') as file:
                    return yaml.safe_load(file)
            elif file_type == PROPERTIES_TYPE:
                with open(file_path, 'r') as file:
                    properties = {}
                    for line in file:
                        if line.strip() and not line.startswith("#"):
                            key, value = line.strip().split('=', 1)
                            properties[key.strip()] = value.strip()
                    return properties
            else:
                logging.error(f"Unsupported file type: {file_type}")
                return None
        except FileNotFoundError:
            logging.error(f"{file_type.upper()} file not found: {file_path}")
            return None
        except Exception as e:
            logging.error(f"Error reading {file_type.upper()} file: {e}")
            return None

    @staticmethod
    def get_property(data, property_path, file_type):
        try:
            if file_type == PROPERTIES_TYPE:
                return data[property_path]
            else:
                properties = property_path.split('.')
                for prop in properties:
                    if file_type == JSON_TYPE or file_type == YAML_TYPE:
                        data = data[prop]
                    elif file_type == XML_TYPE:
                        data = data.find(prop)
                return data.text if file_type == XML_TYPE and data is not None else data
        except (KeyError, TypeError, AttributeError) as e:
            logging.error(f"Property '{property_path}' not found in the {file_type.upper()} data: {e}")
            return None

    @staticmethod
    def read_property(file_path, property_path, file_type):
        data = FileReaders.read_file(file_path, file_type)
        if data:
            property_value = FileReaders.get_property(data, property_path, file_type)
            # if property_value is not None:
            # logging.info(f"Value of '{property_path}': {property_value}")
            return property_value
        return None

    @staticmethod
    def get_json_property(file_path, property_path):
        return FileReaders.read_property(file_path, property_path, JSON_TYPE)

    @staticmethod
    def get_xml_property(file_path, property_path):
        return FileReaders.read_property(file_path, property_path, XML_TYPE)

    @staticmethod
    def get_yaml_property(file_path, property_path):
        return FileReaders.read_property(file_path, property_path, YAML_TYPE)

    @staticmethod
    def get_properties_property(property_path, file_path):
        return FileReaders.read_property(file_path, property_path, PROPERTIES_TYPE)

    @staticmethod
    def get_properties_properties(file_path, *property_paths):
        if isinstance(property_paths, str):
            property_paths = [property_paths]

        properties_values = {}
        for property_path in property_paths:
            value = FileReaders.read_property(file_path, property_path, PROPERTIES_TYPE)
            if value is not None:
                properties_values[property_path] = value

        if len(properties_values) == 1:
            return next(iter(properties_values.values()))
        else:
            return properties_values

# Example usage:
# Reading JSON file
# json_file_path = '../resources/locators/locators.json'
# json_property_path = 'some'
# print(FileReaders.get_json_property(json_file_path, json_property_path))
#
# # Reading XML file
# xml_file_path = '../resources/test_data/test_data.xml'
# xml_property_path = 'some/test'
# print(FileReaders.get_xml_property(xml_file_path, xml_property_path))
#
# # Reading YAML file
# yaml_file_path = '../configuration/env_config.yaml'
# yaml_property_path = 'browser'
# print(FileReaders.get_yaml_property(yaml_file_path, yaml_property_path))
#
# Reading properties file
# properties_file_path = '../resources/sql_queries/sql.properties'
# properties_property_path = 'query'
# print(FileReaders.get_properties_property(properties_property_path, properties_file_path))
# #
# properties_file_path = '../resources/locators/login_page.properties'
# properties_property_path = 'Login_Btn'
# print(FileReaders.get_properties_property(properties_file_path, properties_property_path))
