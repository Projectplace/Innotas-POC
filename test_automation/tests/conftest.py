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


@pytest.fixture()
def do_auth(creds):
    import requests

    session = requests.Session()
    url = 'https://q3.innotas.io/login_sub.pa'
    payload = {'login': creds.username,
               'password': creds.password,
               'tnp': ''}
    session.post(url, data=payload)
    return session.cookies
