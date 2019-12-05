import xlrd
from django.contrib import messages
from django.db import transaction
from django.forms.utils import ErrorList
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import FormView
from wagtail.contrib.redirects.models import Redirect

from wagtail_marketing.forms import RedirectImportForm


class RedirectImportView(FormView):
    form_class = RedirectImportForm

    def post(self, request, *args, **kwargs):
        redirect_import_form = RedirectImportForm(request.POST, request.FILES)
        if redirect_import_form.is_valid():
            before = Redirect.objects.count()
            errors = self.read_and_save_data(
                file_contents=request.FILES['file'], site=redirect_import_form.cleaned_data.get('site'))
            after = Redirect.objects.count()
            if errors:
                messages.error(request=request, message=errors)
            else:
                messages.success(
                    request=request,
                    message=_("Redirects were imported succesfully. {} records inserted.".format(after - before))
                )
        else:
            messages.error(
                request=request, message=redirect_import_form.errors.get('file') or redirect_import_form.errors['site'])

        return redirect('wagtailredirects:index')

    def read_and_save_data(self, file_contents, site):
        errors = ErrorList()
        try:
            book = xlrd.open_workbook(file_contents=file_contents.read())
        except IOError:
            errors.append(_("Something went wrong while reading the file."))
            return errors

        sheet = book.sheets()[0]
        with transaction.atomic():
            for row_id in range(0, sheet.nrows):
                data = sheet.row_values(row_id)
                old_path, redirect_link = data
                if old_path and redirect_link:
                    if old_path.startswith('/') and redirect_link.startswith('/'):
                        # Based on the wagtail.contrib.redirects form validation
                        # https://github.com/wagtail/wagtail/blob/master/wagtail/contrib/redirects/forms.py#L34
                        _old_path = Redirect.normalise_path(old_path)
                        duplicates = Redirect.objects.filter(old_path=_old_path, site=site)
                        if duplicates:
                            errors.append(
                                _(
                                    "Row: {} - Skipped import: the old path is "
                                    "a duplicate of an earlier record.".format(row_id + 1)
                                )
                            )
                        else:
                            Redirect.objects.create(old_path=old_path, redirect_link=redirect_link, site=site)
                    else:
                        errors.append(
                            _("Row: {} - The old path and new path, must both start with /".format(row_id + 1))
                        )
                else:
                    errors.append(_("Row: {} - The old path and new path, must both be filled in.".format(row_id + 1)))
        return errors
