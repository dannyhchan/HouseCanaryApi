import requests
import urllib.parse

class PropertyDataApiService:
  @staticmethod
  def get_property_data(address, zip_code):
    # HouseCanaryAPI requires HTTP Basic Authentication.  In this Demo code, I'm not adding authentication rules to Mockoon-cli.
    # However, it can be done in Mockoon-cli to add request authentication rules to throw 403 http status if needed.

    # Sample HTTP Basic Auth to Request method:
    # username = "xxxxxxx"
    # password = "xxxxxxx"
    # request = requests.get(requestUrl, headers={'Content-Type':'application/json'}, auth=(username, password))
    params = {'address' : address, 'zipcode': zip_code}
    requestUrl = "http://localhost:3004/v2/property/details"
    request = requests.get(requestUrl, params=params, headers={'Content-Type':'application/json'})

    # TODO: Handle request.status_code if it's not 200.
    response = request.json()    

    # Return only the property information from the Json response.  We can decide to return on certain types of properties of the object here.
    # At this point, we will return all information related to the property (excluding the assessment data)
    return response['property/details']['result']['property']

