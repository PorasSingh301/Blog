**Steps to run the project:**

1. Create a virtual environment and clone the git repository
2. Move into the directory blog using command "cd blog" in command line
3. Install the dependencies using the command "pip install -r requirements.txt" in command line
4. Apply the migrations using the command "python manage.py migrate" in command line
5. Create a super user for testing of APIs using the command "python manage.py createsuperuser" in command line
6. Download Postman using the link https://www.postman.com/downloads/
7. Open the application and import the Api collection in the repository named Blog Apis.postman_collection.json
8. To run the development server and test the APIs use the command "python manage.py runserver"
9. Inside the postman collection all the APIs are added along with working examples
10. To use the APIs you will need the authorization key:
    For that use the "Generate auth token API" and get the token from response and use it in all the other APIs by passing it in headers with Key as Authorization and value as Token "token_value"
11. Remember to hit the post APIs after using delete APIs as the record id might mismatch
12. To run the test cases hit the command "python manage.py test" in command line
13. The API documentation on Postman will look something like this
![Screenshot (3)](https://github.com/PorasSingh301/Blog/assets/66668588/e9f72854-219c-418e-9671-3628958aeae6)
