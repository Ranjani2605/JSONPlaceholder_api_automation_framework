from jsonschema import validate

def assert_status_code(response, expected_status_code):
    actual_status_code = response.status_code

    assert actual_status_code == expected_status_code,(
        f"Expected status code {expected_status_code},"
        f"but got {actual_status_code}. "
        f"Response body: {response.text}"
    )


def assert_response_contains_keys(response_json, expected_keys):
    for key in expected_keys:
        assert key in response_json, f"Expected key '{key}' not found in response"


def assert_json_value(response_json, key, expected_value):
    actual_value = response_json.get(key)

    assert actual_value == expected_value, (
        f"Expected '{key}' to be '{expected_value}', "
        f"but got '{actual_value}'"
    )

def assert_json_schema(response_json, schema):
    validate(instance=response_json, schema=schema)