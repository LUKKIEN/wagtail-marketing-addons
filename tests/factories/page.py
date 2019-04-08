import factory
from wagtail.core.models import Page


class PageFactory(factory.DjangoModelFactory):
    seo_title = 'SEO Title'
    search_description = 'Search description'
    title = 'Title'
    depth = 2
    path = 'empty'

    class Meta:
        model = Page
