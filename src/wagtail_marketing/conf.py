from django.conf import settings

DEFAULT_SETTINGS = {
    'TITLE_LENGTH': 70,
    'DESCRIPTION_LENGTH': 123,
}


def get_wagtail_marketing_setting(name):
    return getattr(settings, 'WAGTAIL_MARKETING_{}'.format(name), DEFAULT_SETTINGS[name])
