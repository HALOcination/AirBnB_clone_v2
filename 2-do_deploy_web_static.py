#!/usr/bin/python3
# distributing an archive to my web servers
import os.path
from fabric.api import run, put, env


env.hosts = ["107.23.63.219", "52.87.252.70"]


def do_deploy(archive_path):
    """
    Distributes an archive to a web server.

    Args:
        archive_path (str): path of the archive

    Returns:
        true if deployment is successful, otherwise false
    """
    if not os.path.isfile(archive_path):
        return False

    try:
        file_name = os.path.basename(archive_path)
        name = file_name.split(".")[0]

        put(archive_path, "/tmp/{}".format(file_name))

        run("mkdir -p /data/web_static/releases/{}/".format(name))

        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(file_name, name))

        run("rm /tmp/{}".format(file_name))

        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name))

        run("rm -rf /data/web_static/current")

        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))

        return True

    except Exception as e:
        print("An error occurred:", str(e))
        return False
