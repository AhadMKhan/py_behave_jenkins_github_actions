from Util_Factory.file_readers import FileReaders
from Util_Factory.utility_factory import UtilityFactory


class PropertyReader:

    @staticmethod
    def get_test_data_property(get_test_data_property, test_data_file_path):
        test_data_file_path = UtilityFactory.get_property_file_name(test_data_file_path).lower()
        get_test_data_property = UtilityFactory.make_property_name(get_test_data_property)
        return FileReaders.get_properties_property(get_test_data_property,
                                                   "./resources/test_data/" + test_data_file_path + ".properties")

    @staticmethod
    def get_locator_property(get_locator_property, locator_file_path):
        locator_file_path = UtilityFactory.get_property_file_name(locator_file_path).lower()
        get_locator_property = UtilityFactory.make_property_name(get_locator_property)
        return FileReaders.get_properties_property(get_locator_property,
                                                   "./resources/locators/" + locator_file_path + ".properties")

    @staticmethod
    def get_configuration_property(config_file_path, get_property):
        return FileReaders.get_yaml_property("./configuration/" + config_file_path + ".yaml", get_property)