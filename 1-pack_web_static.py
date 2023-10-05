#!/usr/bin/python3
"""generate a tgz archive from the contents
of the web_staticfolder of the AirBnB Clone repo"""

from datetime import datetime
from fabric.api import local
from os.path import isdir
import os

import subprocess


def do_pack():

    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except (subprocess.CalledProcessError, OSError) as e:
        print(f"An error occurred: {e}")
        return None
