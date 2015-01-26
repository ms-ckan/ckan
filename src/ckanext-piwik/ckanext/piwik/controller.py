from ckan.lib.base import BaseController, config
import ckan.plugins as p

class PiwikController(BaseController):

    def index(self):
    	c = p.toolkit.c
    	c.piwik_host = config.get('ckanext.piwik.host')
    	c.piwik_date = config.get('ckanext.piwik.date')
    	c.piwik_idsite = config.get('ckanext.piwik.idsite')
    	c.piwik_period = config.get('ckanext.piwik.period')
    	c.piwik_token_auth = config.get('ckanext.piwik.token_auth')
        return p.toolkit.render('piwik/index.html')
