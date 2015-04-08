## CKAN 发布时需要注意custom_extension的修改

#### 1. 修改DATA API设置
```
PATH: custom_extension/template/ajax_snippets/api_info.html #(line 14)
```

**QA**: `set datastore_root_url = 'http://civicdataqa.trafficmanager.net/api/action'`

**DEV**: `set datastore_root_url= 'http://civicdatadev.trafficmanager.net/api/action'`

**PROD**:  `set datastore_root_url= 'http://www.civicdata.com/api/action'`


#### 2. 修改disqus的名称设置
```
PATH: custom_extension/template/package/snippets/disqus_comment.html #(line 5)
```

**QA/DEV**: disqus_shortname = 'civicdatadev'

**PROD**: disqus_shortname = 'civicdata'

#### 3. 设置Wordpress的链接

使用Ctrl+F搜索：`http://civicdataqa.cloudapp.net`
```
1) PATH: custom_extension/template/header.html
```
-- 设置**Find Data**, **Why CivicData?**, ** Contact Us**, **Logo Image**的链接为WordPress的网址

```
2) PATH： custom_extension/template/organization/read_base.html
```
-- 设置面包屑导航 **Find Data** 的链接为WordPress的网址

```
3) PATH: custom_extension/template/snippets/home_breadcrumb_item.html
```

-- 返回首页的**HOME图标**，设置为WordPress的网址

```
4) PATH: custom_extension/template/user/logout.html
```

-- 设置**Ajax Logout**，退出登录回到WordPress的网址

```
5) PATH：custom_extension/template/home/layout_new.html
```

-- CivicData 首页海报按钮 **Find Data**，设置Wordpress网址