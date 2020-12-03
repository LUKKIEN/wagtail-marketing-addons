# Getting started

Follow the next steps to start using the wagtail-marketing-addons in your project.

## Requirements

- Wagtail 2.11 or higher

## Installation

Install the package from PyPi:

```bash
pip install wagtail-marketing-addons
```

Add it to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    'wagtail_marketing',
    'wagtail.contrib.modeladmin', # this package and its seo listing depends on the modeladmin
    # ...
]
```

