import json
import xml.etree.ElementTree as ET
import yaml
import logging
from contextlib import contextmanager
import os

from Util_Factory.file_readers import FileReaders


class FileWriter:
    @staticmethod
    def write_json(file_path, data):
        """Write JSON data to a file."""
        try:
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
            logging.info(f"JSON data successfully written to {file_path}")
        except Exception as e:
            logging.error(f"Error writing JSON data to {file_path}: {e}")

    @staticmethod
    def write_xml(file_path, data):
        """Write XML data to a file."""
        try:
            tree = ET.ElementTree(data)
            tree.write(file_path, encoding='utf-8', xml_declaration=True)
            logging.info(f"XML data successfully written to {file_path}")
        except Exception as e:
            logging.error(f"Error writing XML data to {file_path}: {e}")

    @staticmethod
    def write_yaml(file_path, data):
        """Write YAML data to a file."""
        try:
            with open(file_path, 'w') as file:
                yaml.safe_dump(data, file)
            logging.info(f"YAML data successfully written to {file_path}")
        except Exception as e:
            logging.error(f"Error writing YAML data to {file_path}: {e}")

    @staticmethod
    def write_properties(file_path, data):
        """Write properties data to a file."""
        try:
            with open(file_path, 'w') as file:
                for key, value in data.items():
                    file.write(f"{key}={value}\n")
            logging.info(f"Properties data successfully written to {file_path}")
        except Exception as e:
            logging.error(f"Error writing properties data to {file_path}: {e}")

    @staticmethod
    def write_file(file_path, data, file_type):
        """Write data to a file based on its type."""
        if file_type == 'json':
            FileWriter.write_json(file_path, data)
        elif file_type == 'xml':
            FileWriter.write_xml(file_path, data)
        elif file_type == 'yaml':
            FileWriter.write_yaml(file_path, data)
        elif file_type == 'properties':
            FileWriter.write_properties(file_path, data)
        else:
            logging.error(f"Unsupported file type: {file_type}")

    @staticmethod
    def set_property(data, property_path, value, file_type):
        """Set a property in the data structure."""
        try:
            if file_type == 'properties':
                data[property_path] = value
            else:
                properties = property_path.split('.')
                for prop in properties[:-1]:
                    if file_type in ['json', 'yaml']:
                        data = data.setdefault(prop, {})
                    elif file_type == 'xml':
                        found = data.find(prop)
                        if found is None:
                            found = ET.SubElement(data, prop)
                        data = found
                last_prop = properties[-1]
                if file_type in ['json', 'yaml']:
                    data[last_prop] = value
                elif file_type == 'xml':
                    found = data.find(last_prop)
                    if found is None:
                        found = ET.SubElement(data, last_prop)
                    found.text = value
        except Exception as e:
            logging.error(f"Error setting property '{property_path}' in {file_type.upper()} data: {e}")

    @staticmethod
    def set_json_property(file_path, property_path, value):
        """Set a property in a JSON file."""
        data = FileReaders.read_file(file_path, 'json')
        if data is not None:
            FileWriter.set_property(data, property_path, value, 'json')
            FileWriter.write_json(file_path, data)

    @staticmethod
    def set_xml_property(file_path, property_path, value):
        """Set a property in an XML file."""
        data = FileReaders.read_file(file_path, 'xml')
        if data is not None:
            FileWriter.set_property(data, property_path, value, 'xml')
            FileWriter.write_xml(file_path, data)

    @staticmethod
    def set_yaml_property(file_path, property_path, value):
        """Set a property in a YAML file."""
        data = FileReaders.read_file(file_path, 'yaml')
        if data is not None:
            FileWriter.set_property(data, property_path, value, 'yaml')
            FileWriter.write_yaml(file_path, data)

    @staticmethod
    def set_properties_property(file_path, property_path, value):
        """Set a property in a properties file."""
        data = FileReaders.read_file(file_path, 'properties')
        if data is not None:
            FileWriter.set_property(data, property_path, value, 'properties')
            FileWriter.write_properties(file_path, data)


# # Example usage:
# # Setting JSON property
# json_file_path = '../resources/locators/locators.json'
# json_property_path = 'test.another'
# json_value = 'new_value'
# FileWriter.set_json_property(json_file_path, json_property_path, json_value)
#
# # Setting XML property
# xml_file_path = '../resources/test_data/test_data.xml'
# xml_property_path = 'root/some/test'
# xml_value = 'check test'
# FileWriter.set_xml_property(xml_file_path, xml_property_path, xml_value)
#
# Setting YAML property
# yaml_file_path = '../configuration/env_config.yaml'
# yaml_property_path = 'test2'
# yaml_value = 'firefox'
# FileWriter.set_yaml_property(yaml_file_path, yaml_property_path, yaml_value)

# # Setting properties property
# properties_file_path = '../resources/test_data/login_page.properties'
# properties_property_path = 'test_set'
# properties_value = 'check_test'
# FileWriter.set_properties_property(properties_file_path, properties_property_path, properties_value)
