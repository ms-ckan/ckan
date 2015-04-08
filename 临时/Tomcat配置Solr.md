# Tomcat配置Solr

## 准备
- [SOLR 4.10](http://lucene.apache.org/solr/)
- [Tomcat 7](http://tomcat.apache.org)
- JDK 7


**一、配置Tomcat**

修改server.xml文件, 找到`<Connector>`标签，添加`URIEncoding="UTF-8"`，解决中文乱码问题。

```
<Connector port="8080"protocol="HTTP/1.1"
          connectionTimeout="20000"
          redirectPort="8443"  URIEncoding="UTF-8" />
```

**二、配置SOLR**

a) 配置solr.war

将…\solr-4.10.4\dist\solr-4.10.4.war复制到…\tomcat\webapps目录下，改名为solr.war，解压solr.war文件（或先启动tomcat，再关闭，solr.war会自动解压）。

b) 配置solr_home

- 在…\tomcat\webapps\目录下新建文件夹solr_home，然后将…\solr-4.10.4\example\solr目录下的collection1和solr.xml复制到solr_home目录下；

- 打开文件…\tomcat\webapps\solr\WEB-INF\web.xml，找到 <env-entry>标签，将其注释去掉，修改<env-entry-value>的值，改为自己的配置即可，其中，…\webapps\solr_home是之前配置的sole_home路径（如：C:\tomcat\webapps\solr_home）

```
<env-entry>
<env-entry-name>solr/home</env-entry-name>
<env-entry-value>…\webapps\solr_home</env-entry-value>
<env-entry-type>java.lang.String</env-entry-type>
</env-entry>
```

*也可以用下面这种方式，即在…\tomcat\conf\Catalina\localhost目录下添加solr.xml文件，其内容为：*

```
<Context>
<Environment name="solr/home" type="java.lang.String"value=" …\webapps\solr_home" override="true" />
</Context>
```

*注意：无需在Context里添加docBase的路径了，因为你将web工程放在webapps下tomcat默认就有这个路径了，若是再添加就会重复，在tomcat启动日志中会报警告*

c) 打开文件`…\solr_home\collection1\conf\solrconfig.xml`，找到`event="firstSearcher"`的listener，将`<str name="q">staticfirstSearcher warming in solrconfig.xml</str>`改为`<strname="q">*:*</str>`；
若不做此步骤，启动tomcat时，日志有如下异常：
```
org.apache.solr.common.SolrException: undefined field text
```

d) 将…\solr-4.10.4\contrib和…\solr-4.10.4\dist两个目录拷贝到…\tomcat目录下；
若不做此步骤，启动tomcat时，日志有警告：

如果是solr4.2以前的版本，到这里已经配置完成了，由于solr4.3的日志模块与以前的版本不同，所以对于solr4.3还需要配置。

**三、配置solr的log**

（1）将…\solr-4.10.4\example\lib\ext目录下的所有jar包（共5个）复制到…\tomcat\webapps\solr\WEB-INF\lib目录下；

（2）在…\tomcat\webapps\solr\WEB-INF目录下，新建classes文件夹，将…\solr-4.10.4\example\resources目录下的log4j.properties文件复制到刚创建的classes文件夹下；然后，有一个可选的配置log输出目录的操作，因为tomcat默认的相对目录是在bin下面，可根据需要配置logs目录，即修改log4j.properties，将“log4j.appender.file.File=”的值改为“../logs/solr.log”，这样log就会写在…\tomcat\logs目录下

**四、配置完成**

启动tomcat，在浏览器中访问`http://localhost:8080/solr`，若看到solr的管理界面，说明solr配置成功。