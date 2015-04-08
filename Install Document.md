CKAN Offical Document：http://docs.ckan.org/en/latest/

#### 1. Install the required packages
```
sudo apt-get install python-dev postgresql libpq-dev python-pip python-virtualenv git-core solr-jetty openjdk-6-jdk
```

#### 2. Install CKAN into a Python virtual environment

```
mkdir -p ~/ckan/lib
sudo ln -s ~/ckan/lib /usr/lib/ckan
mkdir -p ~/ckan/etc
sudo ln -s ~/ckan/etc /etc/ckan
```

a.Create a Python virtual environment (virtualenv) to install CKAN into, and activate it:

```
sudo mkdir -p /usr/lib/ckan/default
sudo chown 'whoami' /usr/lib/ckan/default
virtualenv --no-site-packages /usr/lib/ckan/default
. /usr/lib/ckan/default/bin/activate
```

b.Install the CKAN source code into your virtualenv. To install the latest stable release of CKAN (CKAN 2.2.1), run:

```
. /usr/lib/ckan/default/bin/activate
pip install -e 'git+https://github.com/ckan/ckan.git@ckan-2.2.1#egg=ckan'
```

c.Install the Python modules that CKAN requires into your virtualenv:

```
pip install -r /usr/lib/ckan/default/src/ckan/requirements.txt
```

d.Deactivate and reactivate your virtualenv, to make sure you’re using the virtualenv’s copies of commands like paster rather than any system-wide installed copies:

```
deactivate
. /usr/lib/ckan/default/bin/activate
```

#### 3. Setup a PostgreSQL database

List existing databases:
```
sudo -u postgres psql -l
```

Check that the encoding of databases is UTF8, if not internationalisation may be a problem. Since changing the encoding of PostgreSQL may mean deleting existing databases, it is suggested that this is fixed before continuing with the CKAN install.

Next you’ll need to create a database user if one doesn’t already exist. Create a new PostgreSQL database user called ckan_default, and enter a password for the user when prompted. You’ll need this password later:

```
sudo -u postgres createuser -S -D -R -P ckan_default
```

Create a new PostgreSQL database, called ckan_default, owned by the database user you just created:

```
sudo -u postgres createdb -O ckan_default ckan_default -E utf-8
```

If PostgreSQL is run on a separate server, you will need to edit postgresql.conf and pg_hba.conf. For PostgreSQL 9.1 on Ubuntu, these files are located in etc/postgresql/9.1/main.

Uncomment the listen_addresses parameter and specify a comma-separated list of IP addresses of the network interfaces PostgreSQL should listen on or ‘*’ to listen on all interfaces. For example,

```
listen_addresses = 'localhost,192.168.1.21'
```

Add a line similar to the line below to the bottom of pg_hba.conf to allow the machine running Apache to connect to PostgreSQL. Please change the IP address as desired according to your network settings.

```
host    all             all             192.168.1.22/32                 md5
```

#### 4. Create a CKAN config file

Create a directory to contain the site’s config files:

```
sudo mkdir -p /etc/ckan/default
sudo chown -R 'whoami' /etc/ckan/
```

Change to the ckan directory and create a CKAN config file:

```
cd /usr/lib/ckan/default/src/ckan
paster make-config ckan /etc/ckan/default/development.ini
```

Edit the development.ini file in a text editor, changing the following options:

sqlalchemy.url
This should refer to the database we created in 3. Setup a PostgreSQL database above:

```
sqlalchemy.url = postgresql://ckan_default:pass@localhost/ckan_default
```

#### 5. Setup Solr

a.Edit the Jetty configuration file (/etc/default/jetty) and change the following variables:

```
NO_START=0            # (line 4)
JETTY_HOST=127.0.0.1  # (line 15)
JETTY_PORT=8983       # (line 18)`
JAVA_HOME=/usr/lib/jvm/java-6-openjdk-amd64/
```

b.Edit the Jetty configuration file(/etc/jetty/start.config) and add a jar:

```
/usr/share/java/tomcat-coyote.jar   #(line 58)
```

Start the Jetty server:

```
sudo service jetty start
```

Open URL: `http://localhost:8983/solr/`

c. Replace the default schema.xml file with a symlink to the CKAN schema file included in the sources.

```
sudo mv /etc/solr/conf/schema.xml /etc/solr/conf/schema.xml.bak
sudo ln -s /usr/lib/ckan/default/src/ckan/ckan/config/solr/schema-2.0.xml /etc/solr/conf/schema.xml
```

Now restart Solr:

```
sudo service jetty restart
```

and check that Solr is running by opening http://localhost:8983/solr/.

d. Finally, change the solr_url setting in your CKAN config file to point to your Solr server, for example:

```
solr_url=http://127.0.0.1:8983/solr  #(vim /etc/ckan/default/development.ini)
```


#### 6. Create database tables
Now that you have a configuration file that has the correct settings for your database, you can create the database tables:

```
. /usr/lib/ckan/default/bin/activate
cd /usr/lib/ckan/default/src/ckan
paster db init -c /etc/ckan/default/development.ini
```

You should see Initialising DB: SUCCESS.

#### 7. Link to who.ini
who.ini (the Repoze.who configuration file) needs to be accessible in the same directory as your CKAN config file, so create a symlink to it:

```
ln -s /usr/lib/ckan/default/src/ckan/who.ini /etc/ckan/default/who.ini
```

#### 8. You’re done!
You can now use the Paste development server to serve CKAN from the command-line. This is a simple and lightweight way to serve CKAN that is useful for development and testing:

```
cd /usr/lib/ckan/default/src/ckan
paster serve /etc/ckan/default/development.ini
```

Open `http://127.0.0.1:5000/` in a web browser, and you should see the CKAN front page.

## Setup Datastore

#### 1. Enable the plugin
Add the datastore plugin to your CKAN config file:

```
ckan.plugins = datastore
```

#### 2. Set-up the database

**Create users and databases**

Create a database_user called datastore_default. This user will be given read-only access to your DataStore database in the Set Permissions step below:

```
sudo -u postgres createuser -S -D -R -P -l datastore_default
```

Create the database (owned by ckan_default), which we’ll call datastore_default:

```
sudo -u postgres createdb -O ckan_default datastore_default -E utf-8
```

**Set URLs**

```
ckan.datastore.write_url = postgresql://ckan_default:pass@localhost/datastore_default
ckan.datastore.read_url = postgresql://datastore_default:pass@localhost/datastore_default

```
**Set permissions**

```
cd /usr/lib/ckan/default/src/ckan/ckanext/datastore/bin
python datastore_setup.py –h

python datastore_setup.py -p postgres ckan_default datastore_default ckan_default ckan_default datastore_default
```

#### 3. Test the set-up

```
. /usr/lib/ckan/default/bin/activate
paster serve /etc/ckan/default/development.ini
curl -X GET "http://127.0.0.1:5000/api/3/action/datastore_search?rchresource_id=_table_metadata"
```

## Setup ckanext-spatial

#### 1. Install PostGIS:

```
sudo apt-get install postgresql-9.3-postgis-2.1  #(postgresql 9.3)
sudo apt-get install postgresql-9.1-postgis  #(postgresql 9.1)
```

#### 2. Run the following commands. The first one will create the necessary tables and functions in the database, and the second will populate the spatial reference table:

```
sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/9.1/contrib/postgis-1.5/postgis.sql
sudo -u postgres psql -d ckan_default -f /usr/share/postgresql/9.1/contrib/postgis-1.5/spatial_ref_sys.sql
```

#### 3. Change the owner to spatial tables to the CKAN user to avoid errors later on:
Open the Postgres console:

```
sudo -u postgres psql
```

Connect to the ckan_default database:
```
postgres=# \c ckan_default
```

Change the ownership for two spatial tables:
```
ALTER TABLE spatial_ref_sys OWNER TO ckan_default;
ALTER TABLE geometry_columns OWNER TO ckan_default;
```

#### 4. Execute the following command to see if PostGIS was properly installed:
```
sudo -u postgres psql -d ckan_default -c "SELECT postgis_full_version()"
```

You should get something like:
```
POSTGIS="1.5.3" GEOS="3.2.2-CAPI-1.6.2" PROJ="Rel. 4.7.1, 23 September 2009" LIBXML="2.7.8" USE_STATS
(1 row)
```

#### 5. Install some other packages needed by the extension dependencies:

```
sudo apt-get install python-dev libxml2-dev libxslt1-dev libgeos-c1
```


