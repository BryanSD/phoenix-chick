import platform

import pecan
from pecan import rest


class HelpController(rest.RestController):

    _custom_actions = {
        'apihealth': ['GET']
    }

    @pecan.expose('json')
    def apihealth(self):
        return {'SystemStatus': [],
                'Status': 'OK',
                'MachineName': platform.node()}
