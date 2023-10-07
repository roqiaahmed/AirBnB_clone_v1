#!/usr/bin/python3
"""
Fabric script that Generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime
import os


def do_pack():
    '''
    Generates a tgz archive from the
    contents of the web_static folder
    '''
    try:
        local('mkdir -p versions')
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        archive_name = 'web_static_{}.tgz'.format(time)
        archive_path = 'versions/{}'.format(archive_name)
        local('tar -czvf {} web_static'.format(archive_path))
        n_path = os.path.getsize(archive_path)
        print("web_static packed: {} -> {}Bytes".format(archive_path, n_path))
    except:
        return None
