import ckan.plugins as p
from ckan.plugins import implements, toolkit

class PiwikPlugin(p.SingletonPlugin):
    implements(p.IConfigurer, inherit=True)
    implements(p.IRoutes, inherit=True)

    def configure(self, config):
        self.site_url = config.get('ckan.site_url')

    def update_config(self, config):
        toolkit.add_template_directory(config, 'theme/templates')
        toolkit.add_public_directory(config, 'theme/public')
        toolkit.add_resource('theme/public', 'ckanext-piwik')

    def before_map(self, map):
        map.connect('/piwik', controller='ckanext.piwik.controller:PiwikController', action='index')

        return map
