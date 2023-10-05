#!/usr/bin/python3
"""
Fabric script that Generates a .tgz archive
"""
from fabric.api import local
from datetime import datetime

def do_pack():
    '''
    Generates a tgz archive from the
    contents of the web_static folder
    '''

    local('mkdir -p versions')
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive_name = 'web_static_{}.tgz'.format(time)
    result = local('tar -cavf versions/{} web_static'.format(archive_name))
    if result.faild:
        return None
    archive_path = 'versions/{}'.format(archive_name)
    return archive_path
