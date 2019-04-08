from django import forms
from django.utils.translation import ugettext_lazy as _
from wagtail.core.models import Site


class RedirectImportForm(forms.Form):
    file = forms.FileField()
    site = forms.ModelChoiceField(queryset=Site.objects.all(), required=False, empty_label=_("All sites"))

    def clean_file(self):
        file = self.cleaned_data['file']

        if not file.name.endswith('.xlsx') and not file.name.endswith('.xls'):
            raise forms.ValidationError(_("Not a supported format. Supported formats: .xlsx, .xls"))

        return file
