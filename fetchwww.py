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
    with cd(os.environ["source_path"]):
        run('tar -xvf /tmp/fetchwww.tar.gz')

    # get wp-content
    get('/tmp/fetchwww.tar.gz', '/tmp')

    # unzip wp-content
    local('tar cvf /tmp/fetchwww.tar.gz -C {0}'.format(os.environ["destination_path"]))

