# HouseCanaryApi

### Requirements
1. Python Version 3.8.14
2. Django Rest Framework
3. Django Rest Framework API Key (Used for API Key Authentication for Server to Server)

### Setup Mock API
1. Mockoon-cli is used for making reponse mocks in this project.  Here is the reference: https://mockoon.com/cli/.  You can install via NPM or use the Desktop version (https://mockoon.com/download/).  I recommend to use the Desktop version as it will be very simple to load up.
2. If using desktop version, open the file `mock-services.json` in the `mock_api` folder of this application.
3. If using command line via NPM install, you will have to run this command `mockoon-cli start <directory>/HouseCanaryApi/mock_api/mock-services.json`.

The `mock-services.json` works with both Desktop or via Command Line.

Note: The `mock-services.json` will start the mock api using port `3004`.  The endpoint URL for the HouseCanaryApi mock is `http://localhost:3004/v2/property/details`
### Start Application

In your terminal (Assuming you cloned the repo and is already in the HouseCanaryApi folder)
<ol>
  <li>Run in virtualenv `source bin/activate`</li>
  <li>Run `pip install -r requirements.txt`</li>
  <li>cd `demo_site`</li>
  <li>Create a super user by running this command `python manage.py createsuperuser`</li>
  <li>Run `python manage.py makemigrations`</li>
  <li>Run `python manage.py migrate`</li>
  <li>run `python manage.py runserver`</li>
  <li>Setup API keys for Authentication or the REST methods won't authenticate.  Log in with the super user account.  The menu should have the API Keys where you can add a new API key.  To Authenticate the REST api calls, you will need to add in the request header with `Authorization` key.  Value needs to be in this format `Api-Key GENERATED_API_KEY`<li>
  <li>On your browser open this URL: `http://127.0.0.1:8000/`</li>
</ol>


## Development
When you add new models, serializers, and urls run the following command in the terminal:
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
