import uuid

from sqlalchemy import Table, Column, MetaData
from sqlalchemy import types
from sqlalchemy.orm import mapper

import ckan.model as model
from ckan.lib.base import *
import datetime


metadata = MetaData()

def make_uuid():
    return unicode(uuid.uuid4())

### Create Table Entity

class Geometry(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

geometry_table = Table('db_geometry', metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('organization_id', types.UnicodeText),
    Column('spatial', types.UnicodeText)
)

mapper(Geometry, geometry_table)

class Contact_Us(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

contact_table = Table('db_contact_us', metadata,
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('name', types.UnicodeText, nullable=False),
    Column('email_address', types.UnicodeText, nullable=False),
    Column('phone_number', types.UnicodeText, nullable=False),
    Column('government_agency', types.UnicodeText),
    Column('job_title', types.UnicodeText),
    Column('message', types.UnicodeText),
    Column('created', types.DateTime, default=datetime.datetime.now())
)

mapper(Contact_Us, contact_table)

### Initialize Tables

def init_tables():
    metadata.create_all(model.meta.engine)

### db_geometry table function

def update_geometry(organization_id, spatial):
    item = _get_geometry(organization_id)
    if item:
        item.organization_id = organization_id
        item.spatial = spatial
        model.Session.add(item)
    else:
        values = {
            "organization_id": organization_id,
            "spatial": spatial
        }
        model.Session.add(Geometry(**values))
    model.Session.commit()

def read_geometry(organization_id):
    return _get_geometry(organization_id)

def _get_geometry(organization_id):
    return model.Session.query(Geometry).filter(Geometry.organization_id == organization_id).first()


### db_contact_us table function

def insert_contact(dict_data):
    '''
    insert contact records
    :param dict_data:
    :return:
    '''
    values = {
        "id": make_uuid(),
        "name": dict_data.get('name'),
        "email_address": dict_data.get('email_address'),
        "phone_number": dict_data.get('phone_number'),
        "government_agency": dict_data.get('government_agency'),
        "job_title": dict_data.get('job_title'),
        "message": dict_data.get('message'),
        "created": datetime.datetime.now()
    }
    model.Session.add(Contact_Us(**values))
    model.Session.commit()

def read_contact(dict_data, offset=0, limit = 10):
    '''
    :param dict_data:
    :return:
    '''
    sql = "SELECT * FROM db_contact_us where 1=1"
    if dict_data.get('id'):
        sql += " AND id = '%s'" % dict_data.get('id')
    if dict_data.get('name'):
        sql += " AND name = '%s'" % dict_data.get('name')
    if dict_data.get('email_address'):
        sql += " AND email_address = '%s'" % dict_data.get('email_address')
    if dict_data.get('phone_number'):
        sql += " AND phone_number = '%s'" % dict_data.get('phone_number')
    sql += " ORDER BY created DESC OFFSET %s LIMIT %s" % (offset, limit)
    return model.Session.execute(sql).fetchall()

def read_count():
    '''
    contact total
    :return:
    '''
    sql = 'SELECT COUNT(*) as total FROM db_contact_us'
    return model.Session.execute(sql).first()

def homepage_organizations():
    '''
    Homepage: Who's publishing data? default: 5 records
    :return:
    '''
    sql = ''' SELECT id, name, title, image_url, count FROM
        (SELECT owner_org, count(id) as count FROM "package"
        WHERE state = 'active' AND private='f' AND owner_org IS NOT NULL
        GROUP BY owner_org ORDER BY count DESC LIMIT 5) AS a
        JOIN "group" AS g ON g.id = a.owner_org ORDER BY count DESC
        '''
    return model.Session.execute(sql).fetchall()