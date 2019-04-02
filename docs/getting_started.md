# Getting started

Follow the next steps to start using the wagtail-marketing-addons in your project.

## Requirements

- Wagtail 2.0 or higher

## Installation

Install the package from PyPi:

```bash
pip install wagtail-marketing-addons
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'wagtail.contrib.modeladmin', # this package depends on the modeladmin
    'wagtail_marketing',
    # ...
]
```

