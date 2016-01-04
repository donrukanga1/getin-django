# README #

**Setup Instructions**

  Clone repo

  ```
  $ git clone https://bitbucket.org/getinug/getin-django.git
  ```

  Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)
  ```
  $ pip install virtualenvwrapper
  ```
  
  Create a virtualenv using 
  ```
  $ mkvirtualenv getin
  ```

  Install requirements
  ```
  $ pip install -r requirments.txt
  ```

  Migrate
  ```
  $ python manage.py migrate
  ```
  
  Run app
  ```
  $ python manage.py runserver
  ``` 