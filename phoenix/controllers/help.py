import platform

from pecan import expose
from pecan.rest import RestController


class HelpController(RestController):

    _custom_actions = {
        'apihealth': ['GET']
    }

    @expose('json')
    def apihealth(self):
        return { 'SystemStatus': [],
                 'Status': 'OK',
                 'MachineName': platform.node() }