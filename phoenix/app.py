import pecan
from phoenix import model


def setup_app(config):

    model.init_model()
    app_conf = dict(config.app)

    return pecan.make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        **app_conf
    )
