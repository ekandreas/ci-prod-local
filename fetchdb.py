
__author__ = 'Andreas Ek'

# import the fabric lib into this script
from fabric.api import *

# connect to sql, make a dump and get it
def fetchdb( private_key_path, server_account, source_host, source_dbname, source_user, source_password, dest_dbname, dest_user, dest_password ):

	print 'Connect to the SQL and create a dump and transfer it to my computer'
	print '=============================================================================='

	print 'set the connection'
	env.key_filename = '{0}'.format(private_key_path)
	env.use_ssh_config = True
	env.user 	= '{0}'.format(source_account)
	env.host_string = '{0}'.format(source_host)

	print 'dump mysql to local tmp'
	run( 'mkdir -p /tmp/fetchdb' )
	run( 'mysqldump --user={0} --password={1} {2] > /tmp/fetchdb/{2}.sql'.format(source_user, source_password, source_dbname) )

	print 'push mysql to local sql'
	run( 'mysql -u {0} -p{1} {2} < /tmp/getsqldump/{3}.sql'.format(dest_user, dest_password, dest_dbname, source_dbname) )


