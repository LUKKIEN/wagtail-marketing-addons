from django import forms
from django.utils.translation import ugettext_lazy as _


class RedirectImportForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data.get('file')

        if not file:
            raise forms.ValidationError(_("No file was selected"))

        if not file.name.endswith('.xlsx') and not file.name.endswith('.xls'):
            raise forms.ValidationError(_("Not a supported format. Supported formats: .xlsx, .xls"))

        return file
