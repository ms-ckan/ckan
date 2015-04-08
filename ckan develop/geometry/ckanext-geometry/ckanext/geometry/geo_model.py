import uuid

from sqlalchemy import Table, Column, MetaData
from sqlalchemy import types
from sqlalchemy.orm import mapper

import ckan.model as model
from ckan.lib.base import *

metadata = MetaData()

def make_uuid():
    return unicode(uuid.uuid4())

class DB_Geometry(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

geometry_table = Table('db_geometry', metadata, 
    Column('id', types.UnicodeText, primary_key=True, default=make_uuid),
    Column('organization_id', types.UnicodeText),
    Column('spatial', types.UnicodeText)
)

mapper(DB_Geometry, geometry_table)

def init_tables():
    metadata.create_all(model.meta.engine)

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
        model.Session.add(DB_Geometry(**values))
    model.Session.commit()

def read_geometry(organization_id):
    return _get_geometry(organization_id)
    
def _get_geometry(organization_id):
    return model.Session.query(DB_Geometry).filter(DB_Geometry.organization_id == organization_id).first()
