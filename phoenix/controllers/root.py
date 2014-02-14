from pecan import expose, response

from phoenix.controllers.v1_0 import V1_0Controller


class RootController(object):

    def __init__(self):
        # Support multiple API versions from the beginning. This should most
        # likely get moved into config
        self.versions = {"v1.0": V1_0Controller()}

    @expose()
    def _lookup(self, primary_key, *remainder):
        try:
            return self.versions[primary_key], remainder
        except KeyError:
            response.status_code = 404
