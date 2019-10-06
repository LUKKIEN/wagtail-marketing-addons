
import pytest
from django.contrib.messages import get_messages
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from wagtail.contrib.redirects.models import Redirect

from tests.factories.accounts import UserFactory
from wagtail_marketing.views import RedirectImportView


@pytest.mark.django_db
class TestRedirectImportView:
    def setup(self):
        self.user = UserFactory(is_superuser=True)

        self.view_url = reverse('redirect_import_view')

    def test_read_and_save_data_check_all_errors(self):
        redirect_import_view = RedirectImportView()
        upload_file = open('tests/data/test.xlsx', 'rb')
        assert Redirect.objects.count() == 0
        result = redirect_import_view.read_and_save_data(
            file_contents=SimpleUploadedFile(upload_file.name, upload_file.read()))
        assert result == [
            'Row: 2 - The old path and new path, must both start with /',
            'Row: 3 - The old path and new path, must both start with /',
            'Row: 4 - The old path and new path, must both be filled in.',
            'Row: 5 - The old path and new path, must both be filled in.',
            'Row: 6 - The old path and new path, must both be filled in.',
            'Row: 7 - The old path and new path, must both start with /',
        ]
        assert Redirect.objects.count() == 2

    def test_post_redirect_import_view_empty_file(self, client):
        client.force_login(user=self.user)

        upload_file = open('tests/data/test-empty.txt', 'rb')

        data = {
            'file': SimpleUploadedFile(upload_file.name, upload_file.read()),
        }

        response = client.post(self.view_url, data=data)
        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1
        assert str(messages[0]) == '<ul class="errorlist"><li>The submitted file is empty.</li></ul>'

    def test_post_redirect_import_view_wrong_file_type(self, client):
        client.force_login(user=self.user)

        upload_file = open('tests/data/test.txt', 'rb')

        data = {
            'file': SimpleUploadedFile(upload_file.name, upload_file.read()),
        }

        response = client.post(self.view_url, data=data)
        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1
        assert str(messages[0]) == '<ul class="errorlist"><li>Not a supported format. Supported formats: .xlsx, .xls</li></ul>'

    def test_post_redirect_import_view_success(self, client):
        client.force_login(user=self.user)

        upload_file = open('tests/data/test-good.xlsx', 'rb')

        data = {
            'file': SimpleUploadedFile(upload_file.name, upload_file.read()),
        }

        response = client.post(self.view_url, data=data)
        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1
        assert str(messages[0]) == 'Redirects were imported succesfully. 5 records inserted.'
