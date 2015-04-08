## CKAN src 目录下的插件说明

#### ckan
安装CKAN的核心目录，管理CKAN的核心功能与实现。升级时需要注意相关改动的内容。

#### ckanext-api
自定义扩展的插件，负责管理新增的接口与服务

#### ckanext-archiver
是ckanext-spatial的依赖包，本身能提供部分功能。但CivicData中没有使用此包相关的功能。

#### ckanext-datastorer
自动解析CSV文件上传到数据库（datastore），但是性能很差。准备使用datapusher插件替换该插件。

#### ckanext-faq
自定义的FAQ插件。只提供一个网页链接，管理FAQs相关的内容。随时可以整合到其他的扩展插件。

#### ckanext-piwik
自定义的PIWIK监控插件。

#### ckanext-spatial
地图搜索与GeoJSON视图的插件。由于跨域的问题，该插件略有改动。

#### ckanext-usmetadata_demo
自定义的元信息插件，由Tanmay提供。

#### ckanext-wordpress
自定义的wordpress插件，提供SSO登录和WordPress需要调用的自定义API。

#### custom_extension
CKAN扩展的静态模板，包含public和template两个文件夹，分别对应ckan/ckan/目录的public和templates两个文件夹。custom_extension中的内容会覆盖ckan/ckan中的内容，但也不例外（follow.js不能覆盖）

#### datapusher
一个更好的上传数据到datastore数据库的插件。用于替换ckanext-datastorer插件。
