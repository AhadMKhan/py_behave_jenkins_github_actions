class UtilityFactory:
    @staticmethod
    def get_property_file_name(text):
        """
        Removes all spaces from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text without spaces.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        return "_".join(text.strip().split())

    @staticmethod
    def remove_spaces(text):
        """
        Removes all spaces from the given text.

        Args:
            text (str): The input text.

        Returns:
            str: The text without spaces.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        return "_".join(text.strip().split())

    @staticmethod
    def make_property_name(text):
        """
        Converts the given text to a valid property name format by replacing spaces with slashes and trimming leading/trailing spaces.

        Args:
            text (str): The input text.

        Returns:
            str: The converted property name.
        """
        if not isinstance(text, str):
            raise ValueError("Input must be a string.")

        return ".".join(text.strip().split())


# print(UtilityFactory.remove_spaces("Test jbascbasc jcjksc  js csabc"))
# print(UtilityFactory.make_property_name("Test jbascbasc jcjksc  js csabc"))
