# HouseCanaryApi - Demo App

This Demo project tries to answer the requirements for the following:

```
Implement the intermediary web service that exposes a custom API for answering the question above, and calls the third-party (HouseCanary) API to get the relevant data.
```

According to my understand, I tried to provide a solution based on the following use case that I understand:

1. In order for the Frontend to prompt an additional question, it must know that based on the home address the "sewer" is "Septic".  This means, that there should be a GET method to retrieve this object from the 3rd Party (HousingCanary).
2. Once the Frontend checks against the object property "sewer" and if the value is "Septic", then a question will be prompted to the user.
3. The user answers a question and the answer to the question is then making a POST call to a custom API to save the data.

Main code logic lies within the `apis` folder and in the `models.py`, `views.py`, `serializers.py`, and `services.py` files.

### Requirements
1. Python Version 3.8.14
2. Django Rest Framework
3. Django Rest Framework API Key (Used for API Key Authentication for Server to Server)

### Use Postman to test the Django API and Mockoon Cli API
Included in the `postman_collections` folder is the exported Postman calls you can use for this project.  There are 2 collections, just import and use them.

1. Django Rest APIs - This is for the REST endpoints to test the Django APIs
2. Mock Service APIs - This is for the Mockoon Cli API Endpoint

### Setup Mock API
1. Mockoon-cli is used for making reponse mocks in this project.  Here is the reference: https://mockoon.com/cli/.  You can install via NPM or use the Desktop version (https://mockoon.com/download/).  I recommend to use the Desktop version as it will be very simple to load up.
2. If using desktop version, open the file `mock-services.json` in the `mock_api` folder of this application.
3. If using command line via NPM install, you will have to run this command `mockoon-cli start <directory>/HouseCanaryApi/mock_api/mock-services.json`.

The `mock-services.json` works with both Desktop or via Command Line.

Note: The `mock-services.json` will start the mock api using port `3004`.  The endpoint URL for the HouseCanaryApi mock is `http://localhost:3004/v2/property/details`
### Start Application

Make sure the Mockoon Cli is running and you can test that by using Postman.

In your terminal (Assuming you cloned the repo and is already in the HouseCanaryApi folder)
<ol>
  <li>Run in virtualenv `source bin/activate`</li>
  <li>Run `pip install -r requirements.txt`</li>
  <li>cd `demo_site`</li>
  <li>Create a super user by running this command `python manage.py createsuperuser`</li>
  <li>Run `python manage.py makemigrations apis`</li>
  <li>Run `python manage.py makemigrations`</li>
  <li>Run `python manage.py migrate`</li>
  <li>run `python manage.py runserver`</li>
  <li>Setup API keys for Authentication or the REST methods won't authenticate.  Log in with the super user account.  The menu should have the API Keys where you can add a new API key.  To Authenticate the REST api calls, you will need to add in the request header with `Authorization` key.  Value needs to be in this format `Api-Key GENERATED_API_KEY`</li>
  <li>On your browser open this URL: `http://127.0.0.1:8000/`</li>
</ol>

### APIs Included in this Demo Project
There are two APIs that are created in this project.

1. `Answers` (http://127.0.0.1:8000/answers/) - There is both REST GET and POST method.  The GET will return all the answers that are submitted via POST.  The POST method will add the record.  

Fields required:
  - questionId (Integer)
  - propertyId (Integer)
  - answer (string)

2. `Property Detail` (http://127.0.0.1:8000/propertydetails) - GET Method to retrieve the property details by passing the following query params:

Query Params:
  - address
  - zipcode

Sample Request `http://127.0.0.1:8000/propertydetails/?address=123%20Main%20St&zipcode=94132`.  This will return the `property` information from the Mocked Canary Housing API.

## Development
When you add new models, serializers, and urls run the following command in the terminal:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Next Steps

In the `services.py`, `PropertyDataApiService` class.  Inside the `get_property_data` method, this can be improved possibly by using a Json -> Json Schema transformation service.  Kind of like using XSLT XML Transformation, but for Json.

In Java, there is a library called `Jolt` which you can define the Json Schema output to map the Json data.  If there are any libraries for Python that does this, there won't necessarily be any code changes but just changing the json schema mappings.  This way, the API code does not have to be impacted at all, but just adjusting the Json schema with any other Json format.  Even if you were to change 3rd party, and the json schema is different, you can use the Json Schema to output to a custom format that is consumed by the Frontend application.
