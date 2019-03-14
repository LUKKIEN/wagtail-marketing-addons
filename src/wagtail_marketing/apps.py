from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WagtailMarketingConfig(AppConfig):
    label = 'wagtail_marketing'
    name = 'wagtail_marketing'
    verbose_name = _("Wagtail Marketing")
