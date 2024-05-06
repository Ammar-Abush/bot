Initialization
Run this command on the requiremtns.txt file : pip install -r requirements.txt.

Inside the settings.py add this at the end: OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'Your Secret key'), make sure you have an environment variable called 'OPEN_API_KEY'

Usage:
1) cd into the directory where manage.py is saved.
2) run python3 manage.py makemigrations
3) python3 manage.py migrate
4) run python3 manage.py runserver
5) copy the url given to you to the browser and add the url path

Url Paths
after the url given to you for example http://localhost:8080/

"chat/" Index path, this is where the user submits the form and recieves an answer from the bot

"chat/login" login path

"chat/logout"

"chat/register"

"chat/history"

Uncomment the lines inside the views.py where methods return Json fromat response. Currently they are commented and another response is returned (HTML page rendering).
