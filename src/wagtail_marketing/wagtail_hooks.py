from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from wagtail.core.models import Page

from wagtail_marketing.conf import get_wagtail_marketing_setting
from wagtail_marketing.helpers import PageAdminURLHelper


class SeoListingAdmin(ModelAdmin):
    model = Page
    menu_label = _("SEO Listing")
    menu_icon = 'fa-search'
    list_display = ('title', 'seo_title', 'search_engine')
    ordering = ('-seo_title', '-search_description')
    search_fields = ('title', 'seo_title')
    url_helper_class = PageAdminURLHelper

    def title(self, obj):
        return obj.get_admin_display_title()
    title.short_description = _("Page title")

    def search_engine(self, obj):
        title = obj.seo_title if obj.seo_title else obj.title
        description = obj.search_description if obj.search_description else ''
        return format_html(
            '<strong>{}</strong><p>{}</p>',
            truncatechars(title, get_wagtail_marketing_setting('TITLE_LENGTH')),
            truncatechars(description, get_wagtail_marketing_setting('DESCRIPTION_LENGTH'))
        )
    search_engine.short_description = _("Search engine example")

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
