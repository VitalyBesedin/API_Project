import json
from utils.cheking import Checking
from utils.api import GoogleMapsApi


"""Creating, editing and deleting a new location"""
class TestCreatePlace:
    def test_create_new_place(self):

        print("Method POST")
        result_post = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)
        Checking.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])

        print("Method GET POST")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        # token = json.loads(result_get.text)   #  getting a list of fields
        # print(list(token))
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])

        print("Method PUT")
        result_put = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])

        print("Method GET PUT")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address',
                                               'types', 'website', 'language'])

        print("Method DELETE")
        result_delete = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])

        print("Method GET DELETE")
        result_get = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])


        print("Testing of creating, changing and deleting a new location was successful!!!")
