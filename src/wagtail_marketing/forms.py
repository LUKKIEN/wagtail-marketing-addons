from django import forms


class RedirectImportForm(forms.Form):
    file = forms.FileField()

    def clean_file(self):
        file = self.cleaned_data.get('file')

        if not file:
            raise forms.ValidationError("There needs to be an file selected")

        if not file.name.endswith('.xlsx') and not file.name.endswith('.xls'):
            raise forms.ValidationError("Wrong file type, .xlsx and .xls are supported")

        return file
