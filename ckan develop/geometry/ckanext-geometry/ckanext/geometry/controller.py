from ckan.lib.base import BaseController
import ckan.lib.helpers as h
import geo_model

from ckan.common import request, response

class GeoController(BaseController):
    
    def addition(self, organization_id):
        help_info = '''Add boundaries data for dataset.\n\n :param organization_id: The boundary data identification.\n\n :param spatial: The data must be GeoJSON format, such as: { "type": "Polygon", "coordinates": [ [ [74.898827, 29.394159],[74.898827, 38.453041], [60.50526, 38.453041], [60.50526, 29.394159], [74.898827, 29.394159] ] ] }'''
       
        data = {'help': help_info, 'success': True}
        spatial = request.params.get('spatial', None)

        if (spatial is None) or (len(str(spatial))==0):
            data['success'] = False
            data['error'] = {'message': 'Not Null', '__type': 'Parameter Not Null Error.'}    
        else:         
            geo_model.update_geometry(organization_id, spatial)
            data['result'] = {'message': 'SUCCESS'}

        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)

    def read(self, organization_id):
        help_info = '''Read GeoJSON data by organization_id.\n\n :param organization_id: The boundary data identification.'''
    
        data = {'help': help_info, 'success': True}
        item = geo_model.read_geometry(organization_id)
        if item:
            data['result'] = {
                'id': item.id,
                'organization_id': item.organization_id,
                'spatial': item.spatial
            }
        else:
            data['success'] = False
            data['error'] = {'message': 'Not Found', '__type': 'Not Found Error.'}        

        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)
