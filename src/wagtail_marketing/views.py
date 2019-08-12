import xlrd
from django.contrib import messages
from django.db import transaction
from django.forms.utils import ErrorList
from django.shortcuts import redirect
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView
from wagtail.contrib.redirects.models import Redirect

from wagtail_marketing.forms import RedirectImportForm


class RedirectImportView(TemplateView):
    def post(self, request, *args, **kwargs):
        redirect_import_form = RedirectImportForm(request.POST, request.FILES)

        if redirect_import_form.is_valid():
            before = Redirect.objects.count()
            errors = self.read_and_save_data(file_contents=request.FILES['file'])
            after = Redirect.objects.count()
            if errors:
                messages.error(request=request, message=errors)
            else:
                messages.success(
                    request=request,
                    message=_("Redirects were imported succesfully. {} records inserted.".format(after - before))
                )
        else:
            messages.error(request=request, message=redirect_import_form.errors['file'])

        return redirect('wagtailredirects:index')

    def read_and_save_data(self, file_contents):
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
                old_path = data[0]
                redirect_link = data[1]
                if old_path and redirect_link:
                    if old_path.startswith('/') and redirect_link.startswith('/'):
                        Redirect.objects.get_or_create(old_path=old_path, redirect_link=redirect_link)
                    else:
                        errors.append(
                            _("Row: {} - The old path and new path, must both start with /".format(row_id + 1))
                        )
                else:
                    errors.append(_("Row: {} - The old path and new path, must both be filled in.".format(row_id + 1)))
        return errors
