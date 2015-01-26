from ckan.lib.cli import CkanCommand

import ckan.model as model
import api_model

log = __import__('logging').getLogger(__name__)

class InitDB(CkanCommand):
    """ Initialise the extension's database tables"""
    summary = __doc__.split('\n')[0]
    usage = __doc__
    max_args = 0
    min_args = 0

    def command(self):
        self._load_config()
        model.Session.remove()
        model.Session.configure(bind=model.meta.engine)
        api_model.init_tables()
        log.info("Database initialize. SUCCESS!")
