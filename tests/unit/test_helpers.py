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
        helper = SeoHelper(
            'My mama always said life was like a box of chocolates. You never know what you are gonna get.')
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
        helper = SeoHelper(
            'Page',
            search_description='If your heads were stuffed with straw, like mine, you would probably all live in the '
                               'beautiful places, and then Kansas would have no people at all. It is fortunate for '
                               'Kansas that you have brains.'
        )
        assert helper.truncated_description == 'If your heads were stuffed with straw, like mine, you would probably ' \
                                               'all live in the beautiful places, and then Kansas would have no ' \
                                               'people at all....'

    @override_settings(WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH=30)
    def test_description_truncation_with_setting_override(self):
        helper = SeoHelper(
            'Title',
            search_description='I am content in knowing I am as brave as any best that ever lived, if not braver.'
        )
        assert helper.truncated_description == 'I am content in knowing I a...'

    def test_score_0(self):
        helper = SeoHelper('', search_description='', seo_title='')
        assert helper.score == 0

    def test_score_title_length(self):
        helper = SeoHelper('TitleIsTenPointsWorth', search_description='', seo_title='')
        assert helper.score == 10

    def test_score_title_word_count(self):
        helper = SeoHelper('Title count is four', search_description='', seo_title='')
        assert helper.score == 40

    @override_settings(WAGTAIL_MARKETING_MIN_DESCRIPTION_LENGTH=2)
    @override_settings(WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH=2)
    def test_score_description_length(self):
        helper = SeoHelper('', search_description='Description length', seo_title='')
        assert helper.score == 25

    @override_settings(WAGTAIL_MARKETING_MIN_DESCRIPTION_LENGTH=2)
    @override_settings(WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH=5)
    def test_score_description_length_between(self):
        helper = SeoHelper('', search_description='Des', seo_title='')
        assert helper.score == 50

    def test_score_total(self):
        helper = SeoHelper(
            'This is the title total score',
            search_description='My mama always said life was like a box of chocolates. You never know what you are '
                               'gonna get.',
            seo_title=''
        )
        assert helper.score == 100

    def test_icon_score_0(self):
        helper = SeoHelper('', search_description='', seo_title='')
        assert helper.score == 0
        assert helper.icon == '😱'

    def test_icon_score_lt_35(self):
        helper = SeoHelper('TitleIsTenPointsWorth', search_description='', seo_title='')
        assert helper.score == 10
        assert helper.icon == '😢'

    @override_settings(WAGTAIL_MARKETING_MIN_DESCRIPTION_LENGTH=2)
    @override_settings(WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH=2)
    def test_icon_score_equal_35(self):
        helper = SeoHelper('TitleIsTenPointsWorth', search_description='Description length', seo_title='')
        assert helper.score == 35
        assert helper.icon == '😏'

    def test_icon_score_gt_35_lt_65(self):
        helper = SeoHelper('Title is 50 points worth', search_description='', seo_title='')
        assert helper.score == 50
        assert helper.icon == '😏'

    def test_icon_score_gt_65(self):
        helper = SeoHelper(
            'Title is 50 points worth',
            search_description='My mama always said life was like a box of chocolates. You never know what you'
                               ' are gonna get.',
            seo_title=''
        )
        assert helper.score == 100
        assert helper.icon == '😄'

    @override_settings(WAGTAIL_MARKETING_MIN_TITLE_LENGTH=300)
    @override_settings(WAGTAIL_MARKETING_MIN_DESCRIPTION_LENGTH=2)
    @override_settings(WAGTAIL_MARKETING_MAX_DESCRIPTION_LENGTH=2)
    def test_icon_score_equal_65(self):
        helper = SeoHelper('T I T L E',
                           search_description='Description length',
                           seo_title='')
        assert helper.score == 65
        assert helper.icon == '😏'
