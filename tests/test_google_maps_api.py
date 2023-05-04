from requests import Response
from utils.cheking import Checking
from utils.api import GoogleMapsApi


"""Creating, editing and deleting a new location"""
class TestCreatePlace:
    def test_create_new_place(self):

        print("Method POST")
        #result_post: Response = GoogleMapsApi.create_new_place()
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)

        print("Method GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Method PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print("Method GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print("Method DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print("Method GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
