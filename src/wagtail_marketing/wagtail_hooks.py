from django.conf.urls import url
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _
from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail.core import hooks

from wagtail_marketing.conf import get_page_model, get_wagtail_marketing_setting
from wagtail_marketing.helpers import PageAdminURLHelper, SeoHelper
from wagtail_marketing.views import RedirectImportView


@hooks.register('register_admin_urls')
def urlconf_status_change():
    return [url(r'^redirects/import/', RedirectImportView.as_view(), name='redirect_import_view'), ]


class SeoListingAdmin(ModelAdmin):
    model = get_page_model()
    menu_label = _("SEO Listing")
    menu_icon = 'fa-search'
    list_display = ('admin_display_title', 'seo_title', 'search_engine', 'score')
    list_filter = get_wagtail_marketing_setting('LIST_FILTER')
    ordering = ('-seo_title', '-search_description')
    search_fields = ('title', 'seo_title', 'search_description')
    url_helper_class = PageAdminURLHelper

    def seo_helper(self, obj):
        return SeoHelper(obj.get_admin_display_title(), obj.seo_title, obj.search_description)

    def admin_display_title(self, obj):
        return obj.get_admin_display_title()
    admin_display_title.short_description = _("Content page title")

    def search_engine(self, obj):
        seo = self.seo_helper(obj)
        return format_html(
            '<strong>{}</strong><p>{}</p>',
            seo.truncated_title,
            seo.truncated_description
        )
    search_engine.short_description = _("Search engine example")

    def score(self, obj):
        seo = self.seo_helper(obj)
        return format_html('<span style="font-size: 28px;">{}</span>', seo.icon)
    score.short_description = _("Score")

    def get_queryset(self, request):
        """ Exclude root page from the queryset """
        qs = super().get_queryset(request)
        return qs.exclude(depth=1)


class WagtailMarketingAdminGroup(ModelAdminGroup):
    menu_label = _("Marketing")
    menu_icon = 'fa-magic'
    menu_order = 500
    items = (SeoListingAdmin,)


modeladmin_register(WagtailMarketingAdminGroup)
