import json
import xml.etree.ElementTree as ET
import yaml
import logging

# Constants
JSON_TYPE = 'json'
XML_TYPE = 'xml'
YAML_TYPE = 'yaml'


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
        else:
            logging.error(f"Unsupported file type: {file_type}")
            return None
    except FileNotFoundError:
        logging.error(f"{file_type.upper()} file not found: {file_path}")
        return None
    except Exception as e:
        logging.error(f"Error reading {file_type.upper()} file: {e}")
        return None


def get_property(data, property_path, file_type):
    try:
        properties = property_path.split('.')
        for prop in properties:
            if file_type == JSON_TYPE:
                data = data[prop]
            elif file_type == XML_TYPE:
                data = data.find(prop)
            elif file_type == YAML_TYPE:
                data = data[prop]
        return data.text if file_type == XML_TYPE and data is not None else data
    except (KeyError, TypeError, AttributeError) as e:
        logging.error(f"Property '{property_path}' not found in the {file_type.upper()} data: {e}")
        return None


def read_property(file_path, property_path, file_type):
    data = read_file(file_path, file_type)
    if data:
        property_value = get_property(data, property_path, file_type)
        if property_value is not None:
            logging.info(f"Value of '{property_path}': {property_value}")
        return property_value
    return None


def get_json_property(file_path, property_path):
    return read_property(file_path, property_path, JSON_TYPE)


def get_xml_property(file_path, property_path):
    return read_property(file_path, property_path, XML_TYPE)


def get_yaml_property(file_path, property_path):
    return read_property(file_path, property_path, YAML_TYPE)


# # Example usage:
# # Reading JSON file
# json_file_path = '../resources/locators/locators.json'
# json_property_path = 'some'
# print(get_json_property(json_file_path, json_property_path))
#
# # Reading XML file
# xml_file_path = '../configuration/run_config.yaml'
# xml_property_path = 'web_url'
# print(get_yaml_property(xml_file_path, xml_property_path))
#
# # Reading YAML file
# yaml_file_path = '../resources/test_data/test_data.xml'
# yaml_property_path = 'some'
# print(get_xml_property(yaml_file_path, yaml_property_path))
