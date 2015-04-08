ckan改变的内容列表

#### src/who.ini

添加了单点登录功能

```
plugins =
    ckan.lib.authenticator:OpenIDAuthenticator
    ckan.lib.authenticator:UsernamePasswordAuthenticator
    ckanext.wordpress.lib.sso_authenticator:SSOAuthenticator #(add this line)
```

#### src/production.ini

CKAN的配置文件，随时可能修改

## src/ckan/ckan

**1) ckan/ckan/logic/action/get.py**

user_list接口调用时，因为要隐藏sysadmin字段，因此在这里做了处理

```
for user in query.all():
    result_dict = model_dictize.user_dictize(user[0], context)
    result_dict.pop('sysadmin')  # add this line
    users_list.append(result_dict)
```

**2） ckan/ckan/public/base/javascript/modules/follow.js**

Follow按钮点击时不会自动+1，因此需要修改follow.js解决了这个问题。但将follow.js放到custom_extension目录，则无效。

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

修改了用户块，为了更快的完成加载

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

修改用户流，为了更改的完成加载

```
def _user_activity_query(user_id):
    '''Return an SQLAlchemy query for all activities from or about user_id.'''
    import ckan.model as model
    q = model.Session.query(model.Activity)\
        .filter(or_(model.Activity.user_id == user_id, model.Activity.object_id == user_id))
    return q
```

## src/ckan/ckanext

#### datastore

新增用户接口，必须修改

#### reclinepreview

Grid, Graph, Map的开发，必须修改

#### stats

修改统计记录，必须修改。但该插件可以移除，效果不大。

## src/ckanext-spatial

```
src\ckanext-spatial\ckanext\spatial\public\js\geojson_preview.js
```

为了支持geojson_preview出现的跨域问题，新增/ckanext/cors接口解决这个问题。因此需要修改geojson_preview.js。

