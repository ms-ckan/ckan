# CivicData.com Restart Solutions

## SOLR Error

- @Author Email: sion.qi@missionsky.com
- @Version: 1.0.0
- @Date: 2015-03-19
- @State Description: Only let the server running. We will continue to follow up and fix it.

Error Description:
```
[error] org.apache.lucene.store.LockObtainFailedException: Lock obtain timed out: NativeFSLock@/var/lib/solr/data/index/write.lock
```

Apache logs:

```
[Tue Mar 17 05:16:30 2015] [error] org.apache.lucene.store.LockObtainFailedException: Lock obtain timed out: NativeFSLock@/var/lib/solr/data/index/write.lock
[Tue Mar 17 05:16:30 2015] [error] SearchIndexError: Solr returned an error: 500 Lock obtain timed out: NativeFSLock@/var/lib/solr/data/index/write.lock  org.apache.lucene.store.LockObtainFailedException: Lock obtain timed out: NativeFSLock@/var/lib/solr/data/index/write.lock \tat org.apache.lucene.store.Lock.obtain(Lock.java:84) \tat org.apache.lucene.index.IndexWriter.<init>(IndexWriter.java:1098) \tat org.apache.solr.update.SolrIndexWriter.<init>(SolrIndexWriter.java:84) \tat org.apache.solr.update.UpdateHandler.createMainIndexWriter(UpdateHandler.java:101) \tat org.apache.solr.update.DirectUpdateHandler2.openWriter(DirectUpdateHandler2.java:171) \tat org.apache.solr.update.DirectUpdateHandler2.addDoc(DirectUpdateHandler2.java:219) \tat org.apache.solr.update.processor.RunUpdateProcessor.processAdd(RunUpdateProcessorFactory.java:61) \tat org.apache.solr.update.processor.LogUpdateProcessor.processAdd(LogUpdateProcessorFactory.java:115) \tat org.apache.solr.handler.XMLLoader.processUpdate(XMLLoader.java:157) \tat org.apache.solr.handler.XMLLoader.load(XMLLoader.java:79) \tat org.apache.solr.handler.ContentStreamHandlerBase.handleRequestBody(ContentStreamHandlerBase.java:58) \tat org.apache.solr.handler.RequestHandlerBase.handleRequest(RequestHandlerBase.java:129) \tat org.apache.solr.core.SolrCore.execute(SolrCore.java:1376) \tat org.apache.solr.servlet.SolrDispatchFilter.execute(SolrDispatchFilter.java:365) \tat org.apache.solr.servlet.SolrDispatchFilter.doFilter(SolrDispatchFilter.java:260) \tat org.mortbay.jetty.servlet.ServletHandler$CachedChain.doFilter(ServletHandler.java:1157) \tat org.mortbay.jetty.servlet.ServletHandler.handle(ServletHandler.java:388) \tat org.mortbay.jetty.security.SecurityHandler.handle(SecurityHandler.java:216) \tat org.mortbay.jetty.servlet.SessionHandler.handle(SessionHandler.java:182) \tat org.mortbay.jetty.handler.ContextHandler.handle(ContextHandler.java:766) \tat org.mortbay.jetty.webapp.WebAppContext.handle(WebAppContext.java:418) \tat org.mortbay.jetty.handler.ContextHandlerCollection.handle(ContextHandlerCollection.java:230) \tat org.mortbay.jetty.handler.HandlerCollection.han - <html>
[Tue Mar 17 05:16:30 2015] [error] <title>Error 500 Lock obtain timed out: NativeFSLock@/var/lib/solr/data/index/write.lock
```

Solutions:

Step 1. Logged into SOLR server

```
host: civicdatadb.cloudapp.net
user: opendatadb
pass: Accela123!
```

Step 2. Delete write.lock file

```
sudo su
rm /var/lib/solr/data/index/write.lock #(please check it's exist.)
```

Step 3. Restart JETTY server
```
service jetty restart #(root user)
sudo service jetty restart #(opendatadb user)
```



