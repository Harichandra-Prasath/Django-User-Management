### Instruction
- Install the requirements from requirements.txt
- Create a .env file with local mongodb database name and path to serviceaccountkey from firebase
- Run python manage.py makemigrations api
- Run python manage.py migrate
- Run python manage.py runserver
- You are now set up

### Endpoints
- /api/accounts/register/ -- To register an account 
- /api/accounts/login/ -- To get the custom_token
- /api/accounts/profile/<id>/view -- To see the Profile
- /api/accounts/profile/<id>/edit -- To edit the profile
- For last two endpoints Authorization header should be Bearer $(custom_token)