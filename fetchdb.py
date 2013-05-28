__author__ = 'Andreas Ek, Flowcom AB'

# import the fabric lib into this script
from fabric.api import *

# connect to sql, make a dump and get it
def fetchdb():

		print env

    # expects environment variables as parameters from Jenkins

    private_key_path = env.private_key_path
    server_host = env.server_host
    server_account = env.server_account
    server_password = env.server_password

    source_dbname = env.source_dbname
    source_user = env.source_user
    source_password = env.source_password

    dest_dbname = env.dest_dbname
    dest_user = env.dest_user
    dest_password = dest_password


    # connect to the SQL and create a dump and transfer it to my computer

    # set the connection
    env.key_filename = private_key_path
    env.use_ssh_config = True
    env.user = server_account

    if server_password:
        env.password = server_password

		# change host now!
    env.host_string = server_host

    # dump mysql to local tmp
    run('mysqldump --user={0} --password={1} {2} > /tmp/{2}.sql'.format(source_user,
                                                                        source_password,
                                                                        source_dbname))

    # get the mysql dump file to local tmp
    get('/tmp/{0}.sql'.format(source_dbname), '/tmp')

    # push mysql to local sql
    local('/Applications/MAMP/Library/bin/mysql -u {0} -p{1} {2} < /tmp/{3}.sql'.format(dest_user,
                                                                                        dest_password,
                                                                                        dest_dbname,
                                                                                        source_dbname))


