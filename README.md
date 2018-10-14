# Beautifulai_lms
An LMS to assist me to prepare and add content for AI in python

**Note:** _It's pretty easy to setup the application, just make sure that you have the following dependencies setup on your system:_
 * Python 3.6 or higher
 * Django 2.1
 * mysqlclient 1.13
 * pip
 * pipenv (I am using pipenv rather than virtualenv,although virtualenv can also be used to setup the project)
 
## Python setup
To setup python v=on windows, linux or mac, visit the official [Python](https://www.python.org/) website for more information.
 
 ## Django 2.1 setup
 * Navigate to your favorite folder.
 * Make sure you have pip installed on your system  and you are able to locate pip from you command line, if not make sure that pip is downloaded and added in your environment variables.
 * After setting up pip, use ```python pip install pipenv ``` to setup pipenv(for setting up virtual environments).
 * After you are done setting up pipenv, run the following command to start your virtual environment, ```python pipenv shell ```.
 * The above setps will setup the virtual environment on your system.
 * Now, use the following command to install django on you system ``python pip install django==2.1 (specially for version 2.1) ```python.
 * After the download is complete, to create a new project use the following command ```python django-admin startproject {name_of_the project} ```python.
 * ***_Learning purpose_* Since you alreay have a project that is **beautifulai_lms** just take a pull of the code and paste it in your directory.
 * Make sure to edit the _settings.py_ file in the project folder, just provide your mysql and DB credentials.
 
 ## mysqlclient 1.13
 * To setup mysqlclient 1.13 download .whl(package in the wheel format, for python), follow the link [mysqlclient-1.3.13-cp36-cp36m-win_amd64](https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient).
 * Run the following command in your command prompt to setup mysqlclient ```python pip install {file_name} ```python.
 
 After everything is setup run the migration using the following command:
```python
python manage.py migrate
```

The above command would create tables in your database, useyour favorite tool too check if all the tables are setup or not (10 tables would be there).

After this create a superuser to fire up django admin, use te following command to do it:
```python
python manage.py createsuperuser
```
Provide the credentials you want to use as your preferred login credentials.

That's it, run the following command to fire up the server,
```python
python manage.py runserver
```

_*If all went well use the URL provided in the command line to access the frontend, and then append ```python /admin``` to the URL to access the administration._