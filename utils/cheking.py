"""Methods for checking the responses of our requests"""
from requests import Response


class Checking:

    """Methods for checking the status code"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print("Successfully!!! Statud code:", response.status_code)
        else:
            print("Failure!!! Statud code:", response.status_code)

