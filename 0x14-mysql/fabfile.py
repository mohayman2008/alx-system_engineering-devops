#!/usr/bin/python3
"""Fabric script to Setup MySQL on the remote servers"""
from datetime import datetime
import os

from fabric.api import env, local, run, sudo, put, hosts

env.user = 'ubuntu'
web1 = '54.90.15.29'
web2 = '18.207.207.53'
env.hosts = [web1, web2]


def install_mysql():
    '''Install MySQL on the remote servers'''

    k_server = 'hkp://pgp.mit.edu'
    key = '3A79BD29'
    if (sudo(f'apt-key adv --keyserver {k_server} --recv-keys {key}').failed):
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
    if (sudo(f'mysql < /tmp/source.sql').failed):
        return False
    run('rm -f /tmp/source.sql')

    if (sudo(f'ufw allow from {web2} to any port 3306').failed):
        return False

    print('MySQL Configuration was done successfully.\n')
    return True


def automate():
    '''Automate MySQL servers installing and configuration'''

    if (not install_mysql()):
        return False
    if (not config_mysql()):
        return False
    if (not config_mysql_source()):
        return False
    
    print('All tasks were executed successfully.\n')
    return True
