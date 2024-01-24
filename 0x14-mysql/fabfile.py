#!/usr/bin/python3
"""Fabric script to Setup MySQL on the remote servers"""
from datetime import datetime
import os

from fabric.api import (env, local, run, sudo, put, prompt, hosts, execute,
                        runs_once)

env.user = 'ubuntu'
web1 = '52.91.120.176'
web2 = '52.23.245.87'
env.hosts = [web1, web2]


def install_mysql():
    '''Install MySQL on the remote servers'''

    k_server = 'hkp://pgp.mit.edu'
    keys = ['3A79BD29', 'A8D3785C', 'B7B3B788A8D3785C']
    for key in keys:
        cmd = f'apt-key adv --keyserver {k_server} --recv-keys {key}'
        if (sudo(cmd).failed):
            return False

    repo = 'deb http://repo.mysql.com/apt/ubuntu/ bionic mysql-5.7'
    if (sudo(f"add-apt-repository '{repo}'").failed):
        return False

    if (sudo("apt-get update").failed):
        return False
    pkgs = "mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*"
    if (sudo(f"apt install -y -f {pkgs}").failed):
        return False

    print('Installed successfully.\n')
    return True


def config_mysql():
    '''Configure MySQL servers on the remote servers'''

    put('configure.sql', '/tmp/configure.sql')
    if (sudo(f'mysql < /tmp/configure.sql').failed):
        return False
    run('rm -f /tmp/configure.sql')

    print('MySQL Configuration was done successfully.\n')
    return True


@hosts(web1)
def config_mysql_source():
    '''Configure MySQL servers on the remote servers'''

    put('source.sql', '/tmp/source.sql')
    if (sudo('mysql < /tmp/source.sql').failed):
        return False
    run('rm -f /tmp/source.sql')

    if (sudo(f'ufw allow from {web2} to any port 3306').failed):
        return False

    if (sudo('service mysql restart').failed):
        return False

    print('MySQL Source Configuration was done successfully.\n')
    return True


@hosts(web2)
def config_mysql_replica():
    '''Configure the replica MySQL servers on web2'''
    log_pos = prompt("Please enter MASTER_LOG_POS: ", validate=r"[0-9]+")

    config = f"""
-- Configure MySQL Replication on the source server

-- Set the master server
CHANGE MASTER TO
MASTER_HOST='\\''{web1}'\\'',
MASTER_USER='\\''replica_user'\\'',
MASTER_PASSWORD='\\''replicate'\\'',
MASTER_LOG_FILE='\\''mysql-bin.000001'\\'',
MASTER_LOG_POS={log_pos};

# Start the replication
START SLAVE;
"""
    if (sudo(f"echo '{config}' | mysql").failed):
        return False

    if (sudo('service mysql restart').failed):
        return False

    print('MySQL Replica Configuration was done successfully.\n')
    return True


@runs_once
def automate():
    '''Automate MySQL servers installing and configuration'''

    if (not execute(install_mysql)):
        return False
    if (not execute(config_mysql)):
        return False
    if (not execute(config_mysql_source, hosts=web1)):
        return False
    # if (not execute(config_mysql_replica, hosts=web2)):
    #     return False

    print('All tasks were executed successfully.\n')
    return True
