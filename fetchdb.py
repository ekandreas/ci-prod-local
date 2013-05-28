
__author__ = 'Andreas Ek'

# import the fabric lib into this script
from fabric.api import *

# connect to sql, make a dump and get it
def fetchdb( account, host, sqluser, sqlpassword, sql2user, sql2password ):

	print 'Connect to the SQL and create a dump and transfer it to my computer'
	print '=============================================================================='

	print 'set the connection'
	env.use_ssh_config = True
	env.user 	= '{0}'.format(account)
	env.host_string = '{0}'.format(host)

	print 'dump mysql to local tmp'
	run( 'mkdir -p /tmp/getsqldump' )
	run( 'mysqldump --user={0} --password={1} minarete > /tmp/getsqldump/minarete.sql'.format(sqluser, sqlpassword) )

	print 'push mysql to local sql'
	run( 'mysql -u {0} -p{1} minarete2 < /tmp/getsqldump/minarete.sql'.format(sql2user, sql2password) )


