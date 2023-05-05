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

    """Method for checking the values of required fields in a response to a request"""
    @staticmethod
    def check_json_value(result, field_name, expected_value):
        check = result.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'The value of the {field_name} field is correct!!!')

    """Method for checking the values of required fields in the request response for a given word"""

    @staticmethod
    def check_json_search_word_in_value(result, field_name, search_word):
        check = result.json()
        check_info = check.get(field_name)
        assert search_word in check_info
        print(f'The word {search_word} is present!!!')