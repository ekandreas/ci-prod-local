__author__ = 'Andreas Ek, Flowcom AB'

# import the fabric lib into this script
from fabric.api import *

# to get all environment parameters from Jenkins, use os.environ:
import os

# connect to sql, make a dump and get it
def fetchwww():
    # expects environment variables as parameters from Jenkins

    # connect to the SQL and create a dump and transfer it to my computer

    # set the connection
    env.key_filename = os.environ["private_key_path"]
    env.use_ssh_config = True
    env.user = os.environ["server_account"]

    if os.environ["server_password"]:
        env.password = os.environ["server_password"]

    # change host now!
    env.host_string = os.environ["server_host"]

    # zip wp-content
    run('zip -rq /tmp/fetchwww.zip {0}/wp-content/.'.format(os.environ["source_path"]))

    # get wp-content
    get('/tmp/fetchwww.zip', '/tmp')

    # unzip wp-content
    local('unzip -po /tmp/fetchwww.zip -d /tmp')

    # copy files to destination
    local('cp -R /tmp{0} {1}'.format(os.environ["source_path"],os.environ["destination_path"]))