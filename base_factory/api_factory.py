import requests

from Util_Factory.file_readers import FileReaders


class APIFactory:
    def __init__(self, url, headers=None):
        self.url = url
        self.headers = headers or {"Content-Type": "application/json"}

    def send_request(self, method, payload=None, **kwargs):
        method = method.upper()
        if method not in {"GET", "POST", "PUT", "DELETE", "PATCH"}:
            raise ValueError(f"Unsupported HTTP method: {method}")

        try:
            response = requests.request(method, self.url, headers=self.headers, data=payload, **kwargs)
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
        with open(file_path, "r") as file:
            json_data = file.read()
        return json_data.encode()

# print(APIFactory.get_request_json_file("put_request"))

# import requests
#
#
# class APIFactory:
#     def __init__(self, url):
#         self.url = url
#         self.response = None
#
#     def send_request(self, method, payload=None):
#         method = method.upper()
#         headers = {"Content-Type": "application/json"}
#
#         if method == "GET":
#             self.response = requests.get(self.url, headers=headers)
#         elif method == "POST":
#             self.response = requests.post(self.url, headers=headers, data=payload)
#         elif method == "PUT":
#             self.response = requests.put(self.url, headers=headers, data=payload)
#         elif method == "DELETE":
#             self.response = requests.delete(self.url, headers=headers)
#         elif method == "PATCH":
#             self.response = requests.patch(self.url, headers=headers, data=payload)
#         else:
#             raise ValueError(f"Unsupported HTTP method: {method}")
#
#         return self.response
#
#     def get_status_code(self):
#         if self.response:
#             return self.response.status_code
#         return None
