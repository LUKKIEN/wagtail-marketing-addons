from wagtail.contrib.modeladmin.helpers import PageAdminURLHelper as AbstractPageAdminURLHelper


class PageAdminURLHelper(AbstractPageAdminURLHelper):
    def get_action_url(self, action, *args, **kwargs):
        action_url = super().get_action_url(action, *args, **kwargs)
        if action == 'edit':
            action_url += '#tab-promote'
        return action_url
