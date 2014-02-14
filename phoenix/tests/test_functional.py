from unittest import TestCase
from webtest import TestApp
from phoenix.tests import FunctionalTest


class TestRootController(FunctionalTest):

    def test_get_not_found(self):
        response = self.app.get('/a/bogus/url', expect_errors=True)
        assert response.status_int == 404
