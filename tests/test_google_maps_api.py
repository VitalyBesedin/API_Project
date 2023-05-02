from requests import Response
from utils.api import GoogleMapsApi


"""Creating, editing and deleting a new location"""
class TestCreatePlace:
    def test_create_new_place(self):

        print("Method POST")
        result_post: Response = GoogleMapsApi.create_new_place()


