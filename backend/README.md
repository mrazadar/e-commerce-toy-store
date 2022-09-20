# Python docs
Following this tutorial
https://simpleisbetterthancomplex.com/series/beginners-guide/1.11/

# Setup up python 

### install python 
using homebrew
install python3

### setup virtual enviornemnt 
`using pip3 install virtualenv`

#### create virtual enviornment
`python3 -m /path/to/new/virtual/environment `

#### activate virtaul env
`source /path/to/new/virtual/environment/bin/activate`

#### deactivate virtual env
`deactivate`

#### create a new django project
`python3 startproject my_project_name`

#### create a new app within project
`python3 startapp my_project_name`

#### create models under
app/models.py

#### after adding models run migrations 
`python manage.py migrate`

#### after migrations sync with DB
`python manage.py migrate --run-syncdb`

#### Templates
Serve the HTML templates using templates folder

#### Testing
Write unit test in tests.py inside your sub-apps

#### Static
Render static content via static folder only in DEV mode
Django doesn't serve your static resource instead you should host them somewhare else

#### Django Admin
create super user for your django admin console

`python manage.py createsuperuser`

Username (leave blank to use 'razadar'): razadar
Email address: raza.dar@arbisoft.com
Password: 1234
Password (again): 1234
Superuser created successfully.
