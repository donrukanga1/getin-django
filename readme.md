Clone repo
$ git clone https://bitbucket.org/getinug/getin-django.git
Install virtualenvwrapper $ pip install virtualenvwrapper
Create a virtualenv using $ mkvirtualenv getin
Install requirements $ pip install -r requirments.txt
Sycndb $ python manage.py migrate
Run app $ python manage.py runserver