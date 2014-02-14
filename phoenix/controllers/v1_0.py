from pecan.rest import RestController

from phoenix.controllers.help import HelpController


class V1_0Controller(RestController):

    help = HelpController()
