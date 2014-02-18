from phoenix import tests


class TestHelpController(tests.FunctionalTest):

    def test_apihealth(self):
        response = self.app.get('/v1.0/help/apihealth')
        assert response.status_int == 200
