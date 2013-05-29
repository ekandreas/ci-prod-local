__author__ = 'Andreas Ek, Flowcom AB'

# import the fabric lib into this script
from fabric.api import *

# to get all environment parameters from Jenkins, use os.environ:
import os

# connect to sql, make a dump and get it
def fetchdb():

	# expects environment variables as parameters from Jenkins

	# connect to the SQL and create a dump and transfer it to my computer

	# set the connection
	print 'connecting to mysql server'
	env.key_filename = os.environ["private_key_path"]
	env.use_ssh_config = True
	env.user = os.environ["server_account"]

	if os.environ["server_password"]:
		env.password = os.environ["server_password"]

	# change host now!
	env.host_string = os.environ["server_host"]

	# dump mysql to local tmp
	print 'dumping sql to file'
	run('mysqldump --user={0} --password={1} {2} > /tmp/{2}.sql'.format(os.environ["source_user"],
																																			os.environ["source_password"],
																																			os.environ["source_dbname"]))

  # put the dump locally in a temp folder
	local('mkdir -p /tmp/fetchdb')

	# get the mysql dump file to local tmp
	print 'transfer dump to localhost'
	get('/tmp/{0}.sql'.format(os.environ["source_dbname"]), '/tmp/fetchdb')

	# push mysql to local sql
	print 'restore to local mysql'
	local('/Applications/MAMP/Library/bin/mysql -u {0} -p{1} {2} < /tmp/fetchdb/{3}.sql'.format(os.environ["destination_user"],
																																											os.environ["destination_password"],
																																											os.environ["destination_dbname"],
																																											os.environ["source_dbname"]))

	# search and replace the site name
	print 'search and replace in database'
	local('cd /tmp/fetchdb'):
	local( 'wget https://raw.github.com/interconnectit/Search-Replace-DB/master/searchreplacedb2cli.php' )
  local( 'wget https://raw.github.com/interconnectit/Search-Replace-DB/master/searchreplacedb2.php' )
  local( 'php /tmp/fetchdb/searchreplacedb2cli.php -h localhost -u {1} -p {2} -d {3} -c utf\-8 -s "{4}" -r "{5}"'.format(os.environ["destination_user"],
  																																																					os.environ["destination_password"],
  																																																					os.environ["destination_dbname"],
  																																																					os.environ["source_url"],
  																																																					os.environ["destination_url"]))
