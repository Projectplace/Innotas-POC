class User(object):

    def __init__(self, user_name, identifier):
        self._user_name = user_name
        self._identifier = identifier

    @property
    def user_name(self):
        return self._user_name

    @property
    def identifier(self):
        return self._identifier

    SIGNATURE = {'name': str}

    @classmethod
    def create(cls, name):
        return cls(name, name)
