import json
import os

import requests

from Util_Factory.property_reader import PropertyReader

request_timeout = PropertyReader.get_configuration_property(
    "env_config", "timeout.request"
)


class APIFactory:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers or {"Content-Type": "application/json"}

    def send_request(self, method, payload=None, **kwargs):
        method = method.upper()
        if method not in {"GET", "POST", "PUT", "DELETE", "PATCH"}:
            raise ValueError(f"Unsupported HTTP method: {method}")

        try:
            response = requests.request(
                method,
                self.url,
                headers=self.headers,
                data=payload,
                timeout=request_timeout,
                **kwargs,
            )
            response.raise_for_status()  # Raise HTTPError for bad response status
            return response
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None

    @staticmethod
    def get_status_code(response):
        return response.status_code if response else None

    @staticmethod
    def get_request_json_file(json_file_name):
        file_path = f"./resources/api/request_body/{json_file_name}.json"
        with open(file_path, "r", encoding="utf-8") as file:
            json_data = file.read()
        return json_data.encode()

    @staticmethod
    def save_response_json(response, filename):
        directory = "./resources/api/response_body/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            json_data = response.json()
            status_code = response.status_code
            filepath = os.path.join(directory, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump({"status_code": status_code, "data": json_data}, f, indent=4)
            print(f"Response JSON saved to: {filepath}")
        except ValueError:
            print("Response content is not valid JSON.")
