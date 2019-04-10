from django.template.defaultfilters import truncatechars
from wagtail.contrib.modeladmin.helpers import PageAdminURLHelper as AbstractPageAdminURLHelper

from wagtail_marketing.conf import get_wagtail_marketing_setting


class PageAdminURLHelper(AbstractPageAdminURLHelper):
    def get_action_url(self, action, *args, **kwargs):
        action_url = super().get_action_url(action, *args, **kwargs)
        if action == 'edit':
            action_url += '#tab-promote'
        return action_url


class SeoHelper:
    def __init__(self, page_title, seo_title=None, search_description=None):
        self.page_title = page_title
        self.seo_title = seo_title
        self.search_description = search_description

    @property
    def title(self):
        return self.seo_title or self.page_title

    @property
    def description(self):
        return self.search_description or ''

    @property
    def truncated_title(self):
        return truncatechars(
            self.title,
            get_wagtail_marketing_setting('MAX_TITLE_LENGTH'),
        )

    @property
    def truncated_description(self):
        return truncatechars(
            self.description,
            get_wagtail_marketing_setting('MAX_DESCRIPTION_LENGTH'),
        )

    @property
    def score(self):
        score = 0

        if (
            get_wagtail_marketing_setting('MIN_TITLE_LENGTH') <= len(self.title)
            <= get_wagtail_marketing_setting('MAX_TITLE_LENGTH')
        ):
            score += 10

        title_word_count = self.title.split()
        if (
            get_wagtail_marketing_setting('MIN_TITLE_WORD_COUNT') <= len(title_word_count)
            <= get_wagtail_marketing_setting('MAX_TITLE_WORD_COUNT')
        ):
            score += 40

        if len(self.description) >= get_wagtail_marketing_setting('MIN_DESCRIPTION_LENGTH'):
            score += 25

        if (
            get_wagtail_marketing_setting('MIN_DESCRIPTION_LENGTH') <= len(self.description)
            <= get_wagtail_marketing_setting('MAX_DESCRIPTION_LENGTH')
        ):
            score += 25

        return score

    @property
    def icon(self):
        if self.score == 0:
            return '😱'
        elif self.score < 35:
            return '😢'
        elif self.score > 65:
            return '😄'
        return '😏'
