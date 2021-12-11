# TheEye

Simple application for CA.

## Configuration
- Poetry environment will be used along with python 3.8 and django 3.2.9
- `black` as the code formatter.
- `flake8` for the code quality.
- `isort` to sort the imports.

## Overall system

- There are two main apps:
  - Events:
    - App for the application event instances
  - Sessions_app:
    - App for the event related sessions.

## Models explanation
### Event
- The event model has 4 fields:
  - category: The category of the event (a charfield)
  - name: Name of the event (a charfield)
  - data: A JSON field with the payload.
  - timestamp: A datetime field for storing the date and time of the event.
  - It also has a property type that returns the string category + name.

### Session
- The session model has 2 fields:
  - session_id: Id of the session sent in the body with the event.
  - event: The relationship with the event (foreign key), because different events could have the same session.

- This app was created in order to have an historical record of the event' session. This couldn't be done with the Session model from django.

### Application
- The applications instances will be taken into account as logged users in the system.

### For processing requests in an Atomic way:
 - ATOMIC_REQUESTS: True in settings.py


### For processing the requests
- We are going to use Celery for processing tasks async in the background.
- Celery uses Redis to pass messages between django and celery workers, so we also use Redis.
