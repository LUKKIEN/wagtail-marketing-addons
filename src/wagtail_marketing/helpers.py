from django.template.defaultfilters import truncatechars
from django.utils.functional import cached_property
from django.utils.text import Truncator

from wagtail.contrib.modeladmin.helpers import PageAdminURLHelper as AbstractPageAdminURLHelper
from wagtail_marketing.conf import get_wagtail_marketing_setting


class PageAdminURLHelper(AbstractPageAdminURLHelper):
    def get_action_url(self, action, *args, **kwargs):
        action_url = super().get_action_url(action, *args, **kwargs)
        if action == 'edit':
            action_url += '#tab-promote'
        return action_url


class SeoHelper:
    def __init__(self, page_title, seo_title, search_description):
        self.page_title = page_title
        self.seo_title = seo_title
        self.search_description = search_description

    @cached_property
    def title(self):
        return self.seo_title or self.page_title

    @cached_property
    def description(self):
        return self.search_description or ''

    @cached_property
    def truncated_title(self):
        return truncatechars(
            self.title,
            get_wagtail_marketing_setting('MAX_TITLE_LENGTH'),
        )

    @cached_property
    def truncated_description(self):
        return truncatechars(
            self.description,
            get_wagtail_marketing_setting('MAX_DESCRIPTION_LENGTH'),
        )

    @cached_property
    def score(self):
        score = 0

        if (
            len(self.title) >= get_wagtail_marketing_setting('MIN_TITLE_LENGTH') and 
            len(self.title) <= get_wagtail_marketing_setting('MAX_TITLE_LENGTH')
        ):
            score += 10

        title_word_count = self.title.split()
        if (
            len(title_word_count) >= get_wagtail_marketing_setting('MIN_TITLE_WORD_COUNT') and 
            len(title_word_count) <= get_wagtail_marketing_setting('MAX_TITLE_WORD_COUNT')
        ):
            score += 40

        if (len(self.description) >= get_wagtail_marketing_setting('MIN_DESCRIPTION_LENGTH')):
            score += 25

        if (
            len(self.description) >= get_wagtail_marketing_setting('MIN_DESCRIPTION_LENGTH') and
            len(self.description) <= get_wagtail_marketing_setting('MAX_DESCRIPTION_LENGTH')
        ):
            score += 25

        return score
