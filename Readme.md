Example code for blog post series on How to do BDD in Python

# Django setup
- `django-admin.exe startproject superlists .`
- `python manage.py startapp lists`

# Dependencies
- `pip install behave`
- `pip install django`
- `pip install selenium`
- `pip install unittest-xml-reporting`

# Misc
To run the `behave` tests you will need either the chrome or firefox webdriver or both. Just download them 
and extract them. You can then just at the path to your environment variables or put the executable in 
a folder/directory that is already in the path list.