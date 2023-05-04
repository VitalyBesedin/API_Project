"""Methods for checking the responses of our requests"""
#from requests import Response


class Checking:

    """Methods for checking the status code"""
    @staticmethod
    def check_status_code(result, status_code):
        assert status_code == result.status_code
        print("Successfully!!! Status code:", result.status_code)
        # if response.status_code == status_code:

        # else:
        #     print("Failure!!! Statud code:", response.status_code)

