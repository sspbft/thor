"""Bootstraps a local setup of an app according to config in default.ini."""
from conf import config
from helpers import io
import subprocess
import os

HOST = "localhost"
IP_ADDR = "127.0.0.1"


def bootstrap():
    """Launches a local environment according to specs in default.ini."""
    create_nodes_file()

    cmd = config.get_entrypoint()
    cwd = config.get_app_path()
    env = os.environ.copy()

    for i in range(0, config.get_node_count()):
        env["ID"] = str(i)
        env["PORT"] = str(5000 + i)
        io.create_folder("logs")
        with open("logs/node{i}.log".format(i=i), "w") as f:
            subprocess.Popen(cmd, shell=True, cwd=cwd, stdout=f, stderr=f, 
                             env=env)
    return


def create_nodes_file():
    """Creates nodes.txt and writes it to specified directory."""
    n = config.get_node_count()
    app_path = config.get_app_path()
    hosts_path = config.get_hosts_path()

    contents = ""
    for i in range(0, n):
        contents = contents + \
            "{host},{ip_addr},{port}\n".format(
                host=HOST, ip_addr=IP_ADDR, port=str(5000 + i))

    path = "{app_path}/{hosts_path}".format(
        app_path=app_path, hosts_path=hosts_path)
    io.write_file(path=path, contents=contents)
