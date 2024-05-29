import os
import json


class ResponseSaver:
    @staticmethod
    def save_response_json(response, filename):
        directory = "./resources/api/response_body/"
        if not os.path.exists(directory):
            os.makedirs(directory)

        try:
            json_data = response.json()
            status_code = response.status_code
            filepath = os.path.join(directory, filename)
            with open(filepath, "w") as f:
                json.dump({"status_code": status_code, "data": json_data}, f, indent=4)
            print(f"Response JSON saved to: {filepath}")
        except ValueError:
            print("Response content is not valid JSON.")
