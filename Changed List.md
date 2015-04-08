Team are based plugin model to the development and management. Minimize coupling procedure.

Following ckan modified the content:

#### src/who.ini

Add the function of single sign-on (sso). Wordpress Login Authenticator.

```
plugins =
    ckan.lib.authenticator:OpenIDAuthenticator
    ckan.lib.authenticator:UsernamePasswordAuthenticator
    ckanext.wordpress.lib.sso_authenticator:SSOAuthenticator #(add this line)
```


## src/ckan/ckan

**1) ckan/ckan/logic/action/get.py**

Call the API `/api/action/user_list`, default show all fields, but an user story didn't show 'sysadmin' field. Team add a code to remove the field. (not )

```
for user in query.all():
    result_dict = model_dictize.user_dictize(user[0], context)
    result_dict.pop('sysadmin')  # add this line
    users_list.append(result_dict)
```

**2） ckan/ckan/public/base/javascript/modules/follow.js**

Before the follow button click can't plus/minus one. Team modified follow.js to fixed it. But an issue is moved it to custom_extension similar dir inoperative.

```
_onClickLoaded: function(json) {
			var options = this.options;
			var sandbox = this.sandbox;
			var followNums = $("[data-module=followers]");
			var nums = parseInt(followNums.text());
			options.loading = false;
			this.el.removeClass('disabled');
			if (options.action == 'follow') {
				followNums.html('<span>'+ (++nums) + '</span>');
				options.action = 'unfollow';
				this.el.html('<i class="icon-remove-sign"></i> ' + this.i18n('unfollow')).removeClass('btn-success').addClass('btn-danger');
			} else {
				followNums.html('<span>'+ (--nums) + '</span>');
				options.action = 'follow';
				this.el.html('<i class="icon-plus-sign"></i> ' + this.i18n('follow')).removeClass('btn-danger').addClass('btn-success');
			}
			sandbox.publish('follow-' + options.action + '-' + options.id);
		}
```

**3) ckan/ckan/model/user.py**

Rewrite query, to provide response speed. #(Optional, Performance Optimization)

```
def number_of_edits(self):
    # have to import here to avoid circular imports
    import ckan.model as model
    from sqlalchemy import func
    revisions_q = meta.Session.query(func.count(model.Revision.id)).select_from(model.Revision)
    revisions_q = revisions_q.filter_by(author=self.name)
    return revisions_q.scalar()
```

4) ckan/ckan/model/activity.py

Rewrite query, to provide response speed. #(Optional, Performance Optimization)

```
def _user_activity_query(user_id):
    '''Return an SQLAlchemy query for all activities from or about user_id.'''
    import ckan.model as model
    q = model.Session.query(model.Activity)\
        .filter(or_(model.Activity.user_id == user_id, model.Activity.object_id == user_id))
    return q
```

## src/ckan/ckanext

#### 1. datastore

Datastore API, some modified and add new APIs.

###### Modfied e.g.

1. Maximum download records can be configured.
2. Sorting the donwload file by _id ASC.

```
data_dict = {
        'resource_id': resource_id,
        'limit': request.GET.get('limit', config.get('ckan.limit', '500000')), # modified
        'offset': request.GET.get('offset', 0),
        'sort': request.GET.get('sort', '_id ASC') #add
    }
```

###### Add new APIs.

**/api/action/datastore_search_sql**

Custom search sql, because datastore_search API can't meet demand. So team add the API.

**/api/action/datastore_delete_sql**

Custom delete sql, to privode admin portal.

**/datastore/json/{resource_id}**

Download as json file, the api similar with download as csv file.

###### Why can't extract?

Datastore is ckan offical extension and provides a number of APIs. API implementation has a strong dependence, authorize and logic. So team can't extract it, and upgrade should compare code and testing.


#### 2. reclinepreview

Ckan offical extension, the Grid, Graph and Map's development and implementation.

#### 3. stats

Ckan offical extension, website analysis and statistics.

## src/ckanext-spatial

To solve geojson_preview cross-domain issues, modified the geojson_preview.js

```
src\ckanext-spatial\ckanext\spatial\public\js\geojson_preview.js
```
