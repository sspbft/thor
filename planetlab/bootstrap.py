"""Bootstraps a node to run a specified app on a PlanetLab node."""
from conf import config
import subprocess
import os
import logging
import helpers.ps as ps

logger = logging.getLogger(__name__)


def bootstrap(args):
    """Launches an app instance on a PlanetLab node."""
    # TODO look into metrics later
    # generate_heimdall_sd()
    # if args.metrics:
    #     start_heimdall(args.debug)

    cmd = config.get_entrypoint()
    cwd = config.get_app_path()
    env = os.environ.copy()
    node_id = args.id

    if node_id is None:
        raise ValueError(f"Arg -i|--id must be specified")

    env["ID"] = str(node_id)
    env["API_PORT"] = str(4000 + node_id)
    env["NUMBER_OF_NODES"] = str(config.get_node_count())
    env["NUMBER_OF_BYZANTINE"] = str(config.get_byzantine_count())
    env["WERKZEUG_RUN_MAIN"] = "true"  # no Flask output
    env["NUMBER_OF_CLIENTS"] = "1"
    if args.debug:
        env["DEBUG"] = "true"

    logger.info(f"Starting app on node {node_id}")
    p = subprocess.Popen(cmd, shell=True, cwd=cwd, env=env)
    ps.add_subprocess_pid(p.pid)

    return
