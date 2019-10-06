import pytest
from django.utils.html import format_html
from wagtail.core.models import Page

from tests.factories.page import PageFactory
from wagtail_marketing.helpers import SeoHelper
from wagtail_marketing.wagtail_hooks import SeoListingAdmin


@pytest.mark.django_db
class TestSeoListingAdmin:
    def setup(self):
        self.seolist = SeoListingAdmin()

    def test_seo_helper(self):
        page = PageFactory()
        result = self.seolist.seo_helper(page)

        assert isinstance(result, SeoHelper)
        assert result.seo_title == page.seo_title
        assert result.search_description == page.search_description
        assert result.page_title == page.title

    def test_admin_display_title(self):
        page = PageFactory()
        result = self.seolist.admin_display_title(page)

        assert result == 'Title'

    def test_search_engine(self):
        page = PageFactory()
        result = self.seolist.search_engine(page)

        assert result == format_html(
            '<strong>{}</strong><p>{}</p>',
            page.seo_title,
            page.search_description
        )

    def test_score(self):
        page = PageFactory()
        result = self.seolist.score(page)

        assert result == format_html('<span style="font-size: 28px;">{}</span>', '😱')

    def test_get_queryset_root(self, client):
        Page.objects.delete()
        page = PageFactory(depth=1)
        page.save()
        result = self.seolist.get_queryset(client.request())

        assert len(result) == 0

    def test_get_queryset(self, client):
        Page.objects.delete()
        page = PageFactory()
        result = self.seolist.get_queryset(client.request())

        assert len(result) == 1
        assert result[0] == page
