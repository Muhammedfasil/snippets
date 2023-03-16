# Snippets

**Snippets** is a text saving and retrieval web app built in Django. This app is able to save short text
snippets with a title, timestamp and created user. The snippet can also have a tag. Implemented JWT authentication for getting user.

## Prerequisite

You need to make sure the following things are set before installing the app.

 1. Python version 3.8
 2. Virtual environment package installed

## Installation

Follow these steps to install the app.

 1. Clone the repository
 2. Create a virtual environment using **venv** or **pipenv**
 3. Activate the virtual environment
 4. Install the dependencies

	    pip install -r requirements.txt

 6. run the following command

		python manage.py runserver

## Authentication

**JWT** authentication is implemented. Can add new users using **Django Admin.** Once you created the user you can use the following endpoints to get the ***access token*** and ***refresh token*** 

##### Admin Credentials

	username : admin
	password : As@12345
		
##### Access Token

	 url = http://localhost:8000/api/token/
	 data = {"username" : "your_username", "password" : "your_password"}
	 method = POST
	 return data = {
		 "refresh": "<your refresh token>",
		 "access": "<your access token>"
	 }

##### Refresh Token
	url = http://localhost:8000/api/token/refresh/
	data = {"refresh" : "<your refresh token>"}
	method = POST
	return data = {
		"access": "<your new access token>"
	}

## Snippet APIs

APIs are available for list all snippets, create new snippets, update snippets, get detailed information of a snippet and delete a snippet. All explained below.
##### Overview API
Total number of snippet and list all available snippets with a hyperlink to respective detail APIs.

	Endpoint : http://localhost:8000/api/snippets/
	Method : GET

##### Create API
API to collect the snippet information and save the data to DB.

	Endpoint : http://localhost:8000/api/snippets/
	Method : POST
	Data : title,short_text,tag
	Data Example : {
		"title" : "Python",
		"short_text" : "Python has Django framework",
		"tag" : "Programming"
	}

##### Detail API
API will display the snippet title, content, and timestamp information.

	Endpoint : http://localhost:8000/api/snippet/<snippet_id>
	Method : GET

##### Update API
API to update individual items. Update API should return item detail response.

	Endpoint : http://localhost:8000/api/snippet/<snippet_id>/
	Method : PUT
	Data : title,short_text,tag
	Data Example : {
		"title" : "Python",
		"short_text" : "Python has Django framework",
		"tag" : "Programming"
	}
	
*Note : All fields are required. Give the field which needs to be updated. Rest of the data must remain same. This will be managed by front-end, like "form initial". For Postman we need to type the data.*

##### Delete API
API to delete selected items and return the list of items as response. This endpoint will take a list of snippet ids and deletes them and returns the rest of the snippets as a list. User confirmation should be implemented in the front-end.

	Endpoint : http://localhost:8000/api/snippets/
	Method : DELETE
	Data : {
		"snippet_ids" : <list of snippet ids to delete>
	}
	Data Example : {
		"snippet_ids" : [1,2,3]
	}


## Tag APIs
APIs are available for list tags,snippets linked to the selected tag.

##### Tag List API
API to list tags. It will return the tag id and tag title.

	Endpoint : http://localhost:8000/api/tags/
	Method : GET

##### Tag Detail API
API to return snippets linked to the selected tag.

	Endpoint : http://localhost:8000/api/tags/<tag id>
	Method : GET


## Technical Specifications

	Django version : 4.1.7
	Python Version : 3.8
	Database used  : Sqlite3