Example code for blog post series on How to do BDD in Python

# Running the application
- `python manage.py runserver`
- Navigate to localhost:8000 in your browser

# Environment setup
- `pip install -r requirements.txt`

# Dependencies
- See the requirements text file.

# Running the tests
- Unit tests - `python manage.py test`
- Behavior tests - `behave`

# Misc
To run the `behave` tests you will need either the chrome or firefox webdriver or both. Just download them 
and extract them. You can then add the path to your environment variables or put the executable in 
a folder/directory that is already in the path list.

# Django setup
Initially this was used to generate a web application project that follows
Model View Controller (MVC)
- `django-admin.exe startproject superlists .`
- `python manage.py startapp lists`