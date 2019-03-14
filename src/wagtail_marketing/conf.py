from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


DEFAULT_SETTINGS = {
    'TITLE_LENGTH': 70,
    'DESCRIPTION_LENGTH': 123,
    'PAGE_MODEL': 'wagtailcore.Page',
    'LIST_FILTER': (),
}


def get_wagtail_marketing_setting(name):
    return getattr(settings, 'WAGTAIL_MARKETING_{}'.format(name), DEFAULT_SETTINGS[name])


def get_page_model():
    """
    Return the Page model that is active in this project.
    """
    page = get_wagtail_marketing_setting('PAGE_MODEL')

    try:
        return apps.get_model(page, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("WAGTAIL_MARKETING_PAGE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "WAGTAIL_MARKETING_PAGE_MODEL refers to model '%s' that has not been installed" % page
        )
