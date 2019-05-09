"""Bootstraps a node to run a specified app on a PlanetLab node."""
from conf import config
import subprocess
import os
import logging
import helpers.ps as ps

logger = logging.getLogger(__name__)


def bootstrap(args):
    """Launches an app instance on a PlanetLab node."""
    cmd = config.get_entrypoint()
    cwd = config.get_app_path()
    env = os.environ.copy()

    start_id = args.scale * args.id
    for i in range(args.scale):
        node_id = start_id
        env["ID"] = str(node_id)
        env["API_PORT"] = str(4000 + node_id)
        env["NUMBER_OF_NODES"] = str(config.get_node_count())
        env["NUMBER_OF_BYZANTINE"] = str(config.get_byzantine_count())
        env["WERKZEUG_RUN_MAIN"] = "true"  # no Flask output
        env["NUMBER_OF_CLIENTS"] = args.clients
        if args.debug:
            env["DEBUG"] = "true"
        if args.runsleep:
            env["RUN_SLEEP"] = args.runsleep
        if args.non_selfstab:
            env["NON_SELF_STAB"] = "1"
        if args.start_state:
            env["INJECT_START_STATE"] = "1"

        logger.info(f"Starting app on node {node_id}")
        if args.logpath:
            with open(args.logpath, "w") as f:
                p = subprocess.Popen(cmd, shell=True, cwd=cwd,
                                     stdout=f, stderr=f, env=env)
        else:
            p = subprocess.Popen(cmd, shell=True, cwd=cwd, env=env)
        ps.add_subprocess_pid(p.pid)

        start_id += 1
    return
