import pecan

from phoenix.controllers import v1_0


class RootController(object):

    def __init__(self):
        # Support multiple API versions from the beginning. This should most
        # likely get moved into config
        self.versions = {"v1.0": v1_0.V1_0Controller()}

    @pecan.expose()
    def _lookup(self, primary_key, *remainder):
        try:
            return self.versions[primary_key], remainder
        except KeyError:
            pecan.response.status_code = 404
