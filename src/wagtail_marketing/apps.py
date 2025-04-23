from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class WagtailMarketingConfig(AppConfig):
    label = 'wagtail_marketing'
    name = 'wagtail_marketing'
    verbose_name = _("Wagtail Marketing")

    def ready(self):
        if not self.apps.is_installed('wagtail_modeladmin'):
            raise RuntimeError(
                'You need to register wagtail_modeladmin in your INSTALLED_APPS '
                'in order for wagtail-marketing-addons to work'
            )
