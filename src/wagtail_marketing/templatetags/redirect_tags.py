from django import template
from wagtail.core.models import Site

register = template.Library()


@register.simple_tag
def get_all_sites():
    return Site.objects.all()
