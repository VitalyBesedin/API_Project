#from requests import Response
from utils.api import GoogleMapsApi


"""Creating, editing and deleting a new location"""
class TestCreatePlace:
    def test_create_new_place(self):

        print("Method POST")
        # result_post: Response = GoogleMapsApi.create_new_place()
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")

        print("Method GET")
        result_get = GoogleMapsApi.get_new_place(place_id)



