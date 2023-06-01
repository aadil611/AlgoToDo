# How to run this project

## clone the repository
> git clone https://github.com/aadil611/AlgoToDo.git

## goto cloned project
> cd AlgoToDo

## create a virtual environment
> python3 -m venv env

## activate the virtual env
> source env/bin/activate

## install the requirements
> pip install -r requirements.txt

## apply the migrations
> python manage.py migrate 

## create .env file from .env.sample content
> cat .env.example > .env

## create superuser for testing adminpanel and other apis
provide required details when asked
> python manage.py createsuperuser

## run the server
> python manage.py runserver


# OR [ using docker-compose ]
> docker-compose up
