import pytest

from django.test import override_settings

from wagtail_marketing.helpers import SeoHelper


class TestPageAdminURLHelper:
    pass


class TestSeoHelper:

    def test_page_title_is_returning_by_default(self):
        helper = SeoHelper('My page title')
        assert helper.title == 'My page title'
        assert helper.description == ''

    def test_seo_title_is_returns_before_page_title(self):
        helper = SeoHelper('My page title', 'My seo title')
        assert helper.title == 'My seo title'
        assert helper.description == ''

    def test_description_returns_properly(self):
        helper = SeoHelper('My page title', search_description='My description')
        assert helper.title == 'My page title'
        assert helper.description == 'My description'

    def test_title_truncation_with_the_default_setting(self):
        helper = SeoHelper('My mama always said life was like a box of chocolates. You never know what you are gonna get.')
        assert helper.truncated_title == 'My mama always said life was like a box of chocolates. Yo...'

    @override_settings(WAGTAIL_MARKETING_MAX_TITLE_LENGTH=30)
    def test_title_truncation_with_setting_override(self):
        helper = SeoHelper('Toto, I have a feeling we are not in Kansas anymore.')
        assert helper.truncated_title == 'Toto, I have a feeling we a...'

    @override_settings(WAGTAIL_MARKETING_MAX_TITLE_LENGTH=30)
    def test_seo_title_truncation_with_setting_override(self):
        helper = SeoHelper(
            'Toto, I have a feeling we are not in Kansas anymore.',
            'True courage is in facing danger when you are afraid',
        )
        assert helper.truncated_title == 'True courage is in facing d...'

    def test_description_truncation_with_the_default_setting(self):
        helper = SeoHelper('Page', search_description='If your heads were stuffed with straw, like mine, you would probably all live in the beautiful places, and then Kansas would have no people at all. It is fortunate for Kansas that you have brains.')
        assert helper.truncated_description == 'If your heads were stuffed with straw, like mine, you would probably all live in the beautiful places, and then Kansas would have no people at all....'

    @override_settings(WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH=30)
    def test_description_truncation_with_setting_override(self):
        helper = SeoHelper('Title', search_description='I am content in knowing I am as brave as any best that ever lived, if not braver.')
        assert helper.truncated_description == 'I am content in knowing I a...'
