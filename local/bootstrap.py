"""Bootstraps a local setup of an app according to config in default.ini."""
from conf import config
from helpers import io
from shutil import which
import subprocess
import os
import json
import logging
import helpers.ps as ps

HOST = "localhost"
IP_ADDR = "127.0.0.1"
logger = logging.getLogger(__name__)


def generate_heimdall_sd():
    """
    Generates the service discovery file used by the Prometheus container
    in Heimdall.
    """
    path = config.get_heimdall_sd_path()
    sd = {"targets": [], "labels": {"mode": "local", "job": "bft-list"}}

    # add all instances on Docker host to targets (only in local mode)
    for i in range(0, config.get_node_count()):
        sd["targets"].append("host.docker.internal:{}".format(6000 + int(i)))

    json_string = json.dumps([sd])
    io.write_file(path, json_string)
    return


def create_nodes_file():
    """Creates nodes.txt and writes it to specified directory."""
    n = config.get_node_count()
    app_path = config.get_app_path()
    hosts_path = config.get_hosts_path()

    contents = ""
    for i in range(0, n):
        contents = contents + \
            "{id},{host},{ip_addr},{port}\n".format(
                id=str(i), host=HOST, ip_addr=IP_ADDR, port=str(5000 + i))

    path = "{app_path}/{hosts_path}".format(
        app_path=app_path, hosts_path=hosts_path)
    io.write_file(path=path, contents=contents)


def start_heimdall(debug=False):
    """
    Starts the Heimdall service.

    Given that docker-compose is available and path to Heimdall project root
    is specified, this methods starts heimdall as a subprocess.
    """
    dc = "docker-compose"
    if which(dc) is None:
        raise EnvironmentError("Can't find installation of docker-compose.")

    path = config.get_heimdall_root()
    if io.exists(path):
        if debug:
            p = subprocess.Popen("{} down && {} up".format(dc, dc), shell=True,
                                 cwd=path)
        else:
            with open("logs/heimdall.log", "w") as f:
                p = subprocess.Popen("{} down && {} up".format(dc, dc),
                                     shell=True, cwd=path, stdout=f, stderr=f)
        ps.add_subprocess_pid(p.pid)
        logging.info("Starting Heimdall with PID {}".format(p.pid))
    else:
        raise ValueError("Heimdall root {} does not exists".format(path))


def bootstrap(args):
    """Launches a local environment according to specs in default.ini."""
    create_nodes_file()
    generate_heimdall_sd()
    if args.metrics:
        start_heimdall(args.debug)

    cmd = config.get_entrypoint()
    cwd = config.get_app_path()
    env = os.environ.copy()

    for i in range(0, config.get_node_count()):
        env["ID"] = str(i)
        env["API_PORT"] = str(4000 + i)
        env["NUMBER_OF_NODES"] = str(config.get_node_count())
        env["NUMBER_OF_BYZANTINE"] = str(config.get_byzantine_count())
        env["WERKZEUG_RUN_MAIN"] = "true"  # no Flask output
        env["NUMBER_OF_CLIENTS"] = "1"
        if args.debug:
            env["DEBUG"] = "true"

        # stashing this since this enables writing subprocess logs to files
        # io.create_folder("logs")
        # log_path = config.get_log_path()
        # if not args.debug:
        #     with open("{}/node{}.log".format(log_path, i), "w") as f:
        #         p = subprocess.Popen(cmd, shell=True, cwd=cwd,
        #                              stdin=f, stderr=f, env=env)
        # else:
        logger.info("Starting app on node {}".format(i))
        p = subprocess.Popen(cmd, shell=True, cwd=cwd, env=env)
        ps.add_subprocess_pid(p.pid)

    return
