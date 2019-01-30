"""
Thor CLI.

CLI that bootstraps a PracticalBFT application according to configuration found
in conf/custom|default.ini and command line arguments.
"""

import argparse
from local.bootstrap import bootstrap as local_bootstrap
from helpers.enums import Mode
from conf import config


def check_mode(mode):
    """Validates that the supplied mode is a valid mode."""
    if mode not in Mode.__members__:
        raise argparse.ArgumentTypeError("Only modes [local] and " +
                                         "[planetlab] are allowed.")
    return Mode[mode]


def setup_argparse():
    """Configures CLI and updates conf if options/args are supplied."""
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", help="either [local] or [planetlab]",
                        type=check_mode)
    parser.add_argument("-n", "--nodes", help="total number of nodes",
                        type=int)
    parser.add_argument("-f", "--faulty", help="number of byzantine nodes",
                        type=int)
    parser.add_argument("-p", "--path", help="absolute path to app to run")
    parser.add_argument("-e", "--entrypoint", help="start script for app")
    parser.add_argument("-m", "--metrics", help="start heimdall metrics",
                        action='store_true')
    args = parser.parse_args()

    if args.nodes is not None:
        config.set_node_count(args.nodes)
    if args.faulty is not None:
        config.set_byzantine_count(args.faulty)
    if args.path is not None:
        config.set_app_path(args.path)
    if args.entrypoint is not None:
        config.set_entrypoint(args.entrypoint)

    return args


if __name__ == "__main__":
    args = setup_argparse()

    if args.mode == Mode.local:
        local_bootstrap(args.metrics)
    else:
        raise NotImplementedError
