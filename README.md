Django
The models are the key components of the framework and represent the structure of the data stored , we create models to use database through python
First, create a project in django by "Event_scheduler" name.command: django-admin startproject Event_Scheduler
Then create a app named events by the command: python manage.py startapp Event
create models by adding the field names to it.
Then use migrations to connect it to the db sqllite server
commands: python manage.py makemigrations
         python manage.py migrate
Form is created for creating and updating events 
view can be used to display,create and update too
in template we can create a simple html code to form a page for basic information.
        
