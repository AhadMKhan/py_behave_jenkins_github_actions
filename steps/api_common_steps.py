import json

from behave import given, when, then
from base_factory.api_factory import APIFactory


@given('I have the API endpoint "{url}"')
def step_given_i_have_the_api_endpoint(context, url):
    context.api_factory = APIFactory(url)


@given('I have the payload from JSON file "{json_file_name}"')
def step_given_i_have_the_payload(context, json_file_name):
    context.json_file_name = json_file_name
    context.payload = context.api_factory.get_request_json_file(json_file_name)
    print("Payload:", context.payload)


@when('I send a "{method}" request to the endpoint')
def step_when_i_send_a_request_to_the_endpoint(context, method):
    context.response = context.api_factory.send_request(method,
                                                        payload=context.payload if hasattr(context,
                                                                                           'payload') else None)

    # Save response JSON to a directory if json_file_name exists in the context
    if hasattr(context, 'json_file_name'):
        filename = context.json_file_name + ".json"
    else:
        # Generate a filename based on the request method
        filename = f"{method.lower()}_response.json"

    try:
        context.api_factory.save_response_json(context.response, filename)
    except Exception as e:
        print(f"Failed to save response JSON: {e}")


@then('the status code should be {expected_status_code:d}')
def step_then_the_status_code_should_be(context, expected_status_code):
    actual_status_code = context.api_factory.get_status_code(context.response)
    assert actual_status_code == expected_status_code, (
        f"Expected status code {expected_status_code}, but got {actual_status_code}"
    )