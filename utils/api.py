from utils.http_methods import HttpMethods

"""Methods for Testing Google Maps API"""
base_url = "https://rahulshettyacademy.com"     # Base URL
key = "?key=qaclick123"                         # Parameter for all requests

"""Method for creating a new location"""
class GoogleMapsApi:
    """Method for creating a new location"""
    @staticmethod
    def create_new_place():

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_resource = "/maps/api/place/add/json"  # POST method's resource
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = HttpMethods.post(post_url, json_for_create_new_place)
        print(result_post.text)
        return result_post

    """Method for checking a new location"""

    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"  # GET method's resource
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for changing a new location"""
    def put_new_place(place_id):
        new_address = "100 Lenina street, RU"  # Add var for address that to check it late
        put_resourse = "/maps/api/place/update/json"  # PUT method's resource
        put_url = base_url + put_resourse + key
        print(put_url)
        json_for_update_new_location = {
            "place_id": place_id,

            "address": new_address,  # changed text to var

            "key": "qaclick123"
        }
        result_put = HttpMethods.put(put_url, json_for_update_new_location)
        print(result_put.text)
        return result_put

    """Method for deleting a new location"""

    def delete_new_place(place_id):
        delete_resourse = "/maps/api/place/delete/json"  # DELETE method's resource
        delete_url = base_url + delete_resourse + key
        print(delete_url)
        json_for_delete_new_location = {
            "place_id": place_id
        }
        result_delete = HttpMethods.delete(delete_url, json_for_delete_new_location)
        print(result_delete.text)
        return result_delete




