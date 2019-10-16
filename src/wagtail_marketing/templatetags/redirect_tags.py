from django import template

from ..forms import RedirectImportForm

register = template.Library()


@register.simple_tag
def get_redirect_import_form():
    return RedirectImportForm()
