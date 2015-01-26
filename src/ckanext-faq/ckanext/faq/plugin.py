import ckan.plugins as p
from ckan.plugins import implements, toolkit

class FAQPlugin(p.SingletonPlugin):
    implements(p.IConfigurer, inherit=True)
    implements(p.IRoutes, inherit=True)

    def configure(self, config):
        self.site_url = config.get('ckan.site_url')

    def update_config(self, config):
        toolkit.add_template_directory(config, 'templates')
        toolkit.add_public_directory(config, 'public')

    def before_map(self, map):
        faq_controller = 'ckanext.faq.controller:FAQController'
        map.connect('/faqs', controller=faq_controller, action='index')

        return map
