import pytest


@pytest.fixture()
def creds():

    class Credentials(object):

        @property
        def username(self):
            return ''

        @property
        def password(self):
            return ''

    return Credentials()
