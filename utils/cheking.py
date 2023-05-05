"""Methods for checking the responses of our requests"""
import json


class Checking:

    """Methods for checking the status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Successfully!!! Status code:", result.status_code)

    """Method for validating required fields in a request response"""
    @staticmethod
    def check_json_token(result, expected_value):
        token = json.loads(result.text)
        assert list(token) == expected_value
        print("All fields are present")