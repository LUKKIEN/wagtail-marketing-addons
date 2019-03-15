from django.template.defaultfilters import truncatechars
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from wagtail.contrib.modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

from wagtail_marketing.conf import get_page_model, get_wagtail_marketing_setting
from wagtail_marketing.helpers import PageAdminURLHelper


class SeoListingAdmin(ModelAdmin):
    model = get_page_model()
    menu_label = _("SEO Listing")
    menu_icon = 'fa-search'
    list_display = ('admin_display_title', 'seo_title', 'search_engine')
    list_filter = get_wagtail_marketing_setting('LIST_FILTER')
    ordering = ('-seo_title', '-search_description')
    search_fields = ('title', 'seo_title', 'search_description')
    url_helper_class = PageAdminURLHelper

    def admin_display_title(self, obj):
        return obj.get_admin_display_title()
    admin_display_title.short_description = _("Content page title")

    def search_engine(self, obj):
        title = obj.seo_title or obj.title
        description = obj.search_description or ''
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
