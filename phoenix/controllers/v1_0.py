from pecan import rest

from phoenix.controllers import help


class V1_0Controller(rest.RestController):

    help = help.HelpController()
