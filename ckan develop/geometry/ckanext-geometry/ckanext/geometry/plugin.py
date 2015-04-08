import ckan.plugins as p
from ckan.plugins import implements

class GeoPlugin(p.SingletonPlugin):
    implements(p.IRoutes, inherit=True)

    def before_map(self, map):
        geo_controller = "ckanext.geometry.controller:GeoController"
        map.connect("/geometry/{organization_id}", controller=geo_controller, action="addition")
        map.connect("/geometry/organization/{organization_id}", controller=geo_controller, action="read")
        return map
