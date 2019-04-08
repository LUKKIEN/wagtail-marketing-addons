from django.apps import apps
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

DEFAULT_SETTINGS = {
    'MIN_TITLE_LENGTH': 20,
    'MAX_TITLE_LENGTH': 60,
    'MIN_TITLE_WORD_COUNT': 4,
    'MAX_TITLE_WORD_COUNT': 7,
    'MIN_DESCRIPTION_LENGTH': 70,
    'MAX_DESCRIPTION_LENGTH': 150,
    'PAGE_MODEL': 'wagtailcore.Page',
    'LIST_FILTER': (),
}


def get_wagtail_marketing_setting(name):
    return getattr(settings, 'WAGTAIL_MARKETING_{}'.format(name), DEFAULT_SETTINGS[name])


def get_page_model():
    """
    Return the Page model that is active within the project.
    """
    page = get_wagtail_marketing_setting('PAGE_MODEL')

    try:
        return apps.get_model(page, require_ready=False)
    except ValueError:
        raise ImproperlyConfigured("WAGTAIL_MARKETING_PAGE_MODEL must be of the form 'app_label.model_name'")
    except LookupError:
        raise ImproperlyConfigured(
            "WAGTAIL_MARKETING_PAGE_MODEL refers to model '{}' that has not been installed".format(page)
        )
