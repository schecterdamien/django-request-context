# django-request-context

Django middleware which provide request and g object.
 all of which are accessible everywhere, and thread isolation, just like used in flask. 

## Installing

Install and update using pip:

```
pip install django-request-context
```


## Usage

  1. Add RequestContextMiddleware to MIDDLEWARE in settings.py
  
 ```
 import django_request_context
 
 MIDDLEWARE = [
    ...
    'django_request_context.RequestContextMiddleware',
    ...
    ] 
 ``` 
 
  2. You can get request and g objects anywhere in the project throughout the life cycle of the request.
  just import:
```
from django_request_context import request, g
```

 
## why do you need this?
when your django project is big enough and the function call stack is deep.
if your want to get request object in the bottom of the call stack,
you need to transfer request as parameters layer-by-layer, this can help you get request directly.
the request you import from django-request-context is **readonly** object,
if your want to convey some message you can user g object, this is a **writeable** object.
the behavior of the request and g objects is exactly the same as in the flask.
