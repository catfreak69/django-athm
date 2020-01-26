# django-athm

Django + ATH Móvil proof-of-concept

References

- https://github.com/evertec/athmovil-javascript-api

- https://docs.djangoproject.com/en/3.0/ref/csrf/#ajax

## Concept

1. `pip install django-athm`

2. 

```python
INSTALLED_APPS = [
    ...,
    "django_athm",
]
```

3.

4.

5.

## How To Use

### Accepting payments via ATHM Button in template


**NOTE**: You must have jQuery loaded in your Django template BEFORE you use the ATH template tag.

You can use the following snippet:
```html
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
```

---
---
---

`templates/index.html`
```html

{% load django_athm %}

{% athm_button ATHM_CONFIG %}
```

`settings.py`
```python

# ...

DJANGO_ATHM_SANDBOX_MODE = True # Default: False
DJANGO_ATHM_PUBLIC_TOKEN = 'YOUR_PUBLIC_TOKEN_HERE' # Default: None
DJANGO_ATHM_PRIVATE_TOKEN =  'YOUR_PRIVATE_TOKEN_HERE'

# ...
```

`views.py`
```python
from django.views import render

def example_view(request):
    context = {
         "ATHM_CONFIG": {
            "env": "sandbox",
            "public_token": "sandboxtoken01875617264",
            "lang": "en",
            "total": 1.00,
            "items": [
            {
                "name": "First Item",
                "description": "This is a description.",
                "quantity": "1",
                "price": "1.00",
                "tax": "1.00",
                "metadata": "metadata test"
            }]
        }
    }

    return render(request, "index.html", context=context)
```



