from ckan.lib.base import BaseController
import ckan.lib.helpers as h
import api_model
import mail

from ckan.common import request, response

log = __import__('logging').getLogger(__name__)

class GeoController(BaseController):
    
    def addition(self, organization_id):
        help_info = '''Add boundaries data for dataset.\n\n :param organization_id: The boundary data identification.\n\n :param spatial: The data must be GeoJSON format, such as: { "type": "Polygon", "coordinates": [ [ [74.898827, 29.394159],[74.898827, 38.453041], [60.50526, 38.453041], [60.50526, 29.394159], [74.898827, 29.394159] ] ] }'''
       
        data = {'help': help_info, 'success': True}
        spatial = request.params.get('spatial', None)

        if (spatial is None) or (len(str(spatial))==0):
            data['success'] = False
            data['error'] = {'message': 'Not Null', '__type': 'Parameter Not Null Error.'}    
        else:         
            api_model.update_geometry(organization_id, spatial)
            data['result'] = {'message': 'SUCCESS'}

        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)

    def read(self, organization_id):
        help_info = '''Read GeoJSON data by organization_id.\n\n :param organization_id: The boundary data identification.'''
    
        data = {'help': help_info, 'success': True}
        item = api_model.read_geometry(organization_id)
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

class ContactUsController(BaseController):

    def addition(self):
        help_info = '''Add the customer submits information\n :param name :type string \n :param email_address :type string \n :param phone_number :type string \n :param government_agency :type string \n :param job_title :type string \n :param message :type string \n'''
        data = {'help': help_info, 'success': True}

        # request data
        dict_data = {}
        dict_data['name'] = request.params.get('name', None)
        dict_data['email_address'] = request.params.get('email_address', None)
        dict_data['phone_number'] = request.params.get('phone_number', None)
        dict_data['government_agency'] = request.params.get('government_agency', None)
        dict_data['job_title'] = request.params.get('job_title', None)
        dict_data['message'] = request.params.get('message', None)

        if (dict_data.get('name') is None) or \
                 (dict_data.get('email_address') is None) or \
                 (dict_data.get('phone_number') is None):
            data['success'] = False
            data['error'] = {'message': 'Not Null', '__type': 'Parameter Not Null Error.'}
        else:
            api_model.insert_contact(dict_data)
            data['result'] = {'message': 'SUCCESS'}

            content = '''
            <html><body><h3>Name: <span style="font-weight: normal;">{0}</span></h3>
            <h3>Email Address: <span style="font-weight: normal;">{1}</span></h3><h3>Phone Number: <span style="font-weight: normal;">{2}</span></h3>
            <h3>Government Agency: <span style="font-weight: normal;">{3}</span></h3><h3>Job Title: <span style="font-weight: normal;">{4}</span></h3>
            <h3>Message: <span style="font-weight: normal;">{5}</span></h3></body></html>
            '''.format(dict_data.get('name'), dict_data.get('email_address'),
                       dict_data.get('phone_number'), dict_data.get('government_agency'),
                       dict_data.get('job_title'), dict_data.get('message'))

            # send email
            if (mail.send_mail('{0} Contact CivicData'.format(dict_data.get('name')), content)):
                log.debug('send email success!')
            else:
                log.debug('send email failure!')
            

        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)

    def read(self):
        help_info = '''Read the customer submits information\n :param id :type string \n :param name :type string \n :param email_address :type string \n :param phone_number :type string \n :param offset :type number \n :param limit :type number \n'''
        data = {'help': help_info, 'success': True}

        # request params
        dict_data = {}
        dict_data['id'] = request.params.get('id', None)
        dict_data['name'] = request.params.get('name', None)
        dict_data['email_address'] = request.params.get('email_address', None)
        dict_data['phone_number'] = request.params.get('phone_number', None)
        offset = request.params.get('offset', 0)
        limit = request.params.get('limit', 10)

        items = api_model.read_contact(dict_data, offset, limit)
        if items:
            item_arr = []
            for item in items:
                contact = {
                    "id": item.id,
                    "name": item.name,
                    "email_address": item.email_address,
                    "phone_number": item.phone_number,
                    "government_agency": item.government_agency,
                    "job_title": item.job_title,
                    "message": item.message,
                    "created": str(item.created)
                }
                item_arr.append(contact)

            data['result'] = item_arr
            #data['total'] = api_model.read_count().total
        else:
            data['success'] = False
            data['error'] = {'message': 'Not Found', '__type': 'Not Found Error.'}

        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)


class HomepageController(BaseController):

    def read_homepage_organizations(self):
        help_info = '''Read homepage organizations:Who's publishing data? default: 5 records'''

        data = {'help': help_info, 'success': True}

        items = api_model.homepage_organizations()
        if items:
            item_arr = []
            for item in items:
                orgs = {
                    "id": item.id,
                    "name": item.name,
                    "title": item.title,
                    "image_url": item.image_url,
                    "count": item.count
                }
                item_arr.append(orgs)
            data['result'] = item_arr
        else:
            data['success'] = False
            data['error'] = {'message': 'Not Found', '__type': 'Not Found Error.'}

        response.headers['Content-Type'] = 'application/json;charset=utf-8'
        return h.json.dumps(data)
