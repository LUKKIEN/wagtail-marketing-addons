from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class WagtailMarketingConfig(AppConfig):
    label = 'wagtail_marketing'
    name = 'wagtail_marketing'
    verbose_name = _("Wagtail Marketing")

    def ready(self):
        if not self.apps.is_installed('wagtail.contrib.modeladmin'):
            raise RuntimeError(
                'You need to register wagtail.contrib.modeladmin in your INSTALLED_APPS'
                'in order for wagtail-marketing-addons to work'
            )
