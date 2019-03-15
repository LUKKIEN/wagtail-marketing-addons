from django.template.defaultfilters import truncatechars
from django.utils.functional import cached_property

from wagtail.contrib.modeladmin.helpers import PageAdminURLHelper as AbstractPageAdminURLHelper
from wagtail_marketing.conf import get_wagtail_marketing_setting


class PageAdminURLHelper(AbstractPageAdminURLHelper):
    def get_action_url(self, action, *args, **kwargs):
        action_url = super().get_action_url(action, *args, **kwargs)
        if action == 'edit':
            action_url += '#tab-promote'
        return action_url


class SeoHelper:
    def __init__(self, title, seo_title, search_description):
        self.title = title
        self.seo_title = seo_title
        self.search_description = search_description

    @cached_property
    def truncated_title(self):
        return truncatechars(
            self.seo_title or self.title,
            get_wagtail_marketing_setting('TITLE_LENGTH'),
        )

    @cached_property
    def truncated_description(self):
        return truncatechars(
            self.search_description or '',
            get_wagtail_marketing_setting('DESCRIPTION_LENGTH'),
        )

    @cached_property
    def score(self):
        return None
