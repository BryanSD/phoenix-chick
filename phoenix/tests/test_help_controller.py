from unittest import TestCase
from webtest import TestApp
from phoenix.tests import FunctionalTest


class TestHelpController(FunctionalTest):

    def test_apihealth(self):
        response = self.app.get('/v1.0/help/apihealth')
        assert response.status_int == 200
