
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
            'row: 2 - Old path and redirect link, must both start with /',
            'row: 3 - Old path and redirect link, must both start with /',
            'row: 4 - Old path and redirect link, must both be filled in',
            'row: 5 - Old path and redirect link, must both be filled in',
            'row: 6 - Old path and redirect link, must both be filled in',
            'row: 7 - Old path and redirect link, must both start with /',
            'row: 8 - Old path and redirect link, cannot be the same'
        ]
        assert Redirect.objects.count() == 1

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
        assert str(messages[0]) == '<ul class="errorlist"><li>Wrong file type, .xlsx and .xls are supported</li></ul>'

    def test_post_redirect_import_view_success(self, client):
        client.force_login(user=self.user)

        upload_file = open('tests/data/test-good.xlsx', 'rb')

        data = {
            'file': SimpleUploadedFile(upload_file.name, upload_file.read()),
        }

        response = client.post(self.view_url, data=data)
        messages = list(get_messages(response.wsgi_request))
        assert len(messages) == 1
        assert str(messages[0]) == 'List is imported succesfully, there where 5 inserted'
