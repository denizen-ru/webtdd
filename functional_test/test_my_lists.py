from django.conf import settings
from django.contrib.auth import get_user_model

from functional_test.base import FuncionalTest
from functional_test.server_tools import create_session_on_server
from functional_test.management.commands.create_session import (
    create_pre_authenticated_session)

User = get_user_model()


class MyListTest(FuncionalTest):

    def create_pre_authenticated_session(self, email):
        if self.against_staging:
            session_key = create_session_on_server(self.server_host, email)
        else:
            session_key = create_pre_authenticated_session(email)
        # to set a cookie we need to first visit the domain.
        # 404 pages load the quickest!
        self.browser.get(self.server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session_key,
            path='/',
        ))

    def test_logged_in_users_lists_are_saved_as_my_lists(self):
        email = 'edith@example.com'
        self.browser.get(self.server_url)
        self.wait_to_be_logged_out(email)

        # Edith is a logged-in user
        self.create_pre_authenticated_session(email)
        self.browser.get(self.server_url)
        self.wait_to_be_logged_in(email)
