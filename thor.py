"""
Thor CLI.

CLI that bootstraps a PracticalBFT application according to configuration found
in conf/custom|default.ini and command line arguments.
"""

import argparse
from local.bootstrap import bootstrap as local_bootstrap
from helpers.enums import Mode
from conf import config
import helpers.ps as ps
import helpers.io as io
import signal
import threading
import logging
import sys


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


def on_sig_term(signal, frame):
    """Kills subprocess and terminates Thor on CTRL + C."""
    ps.kill_all_subprocesses()
    sys.exit(0)


def setup_logging():
    """Configures the logging for Thor."""
    log_folder_path = config.get_log_path()
    io.create_folder(log_folder_path)
    log_file_path = "{}/thor.log".format(log_folder_path)
    io.create_file(log_file_path)
    logging.basicConfig(filename=log_file_path,
                        level=logging.INFO)


if __name__ == "__main__":
    args = setup_argparse()
    setup_logging()

    if args.mode == Mode.local:
        local_bootstrap(args.metrics)
        print("All processes launched in background... (CTRL+C to kill)")
        signal.signal(signal.SIGINT, on_sig_term)
        forever = threading.Event()
        forever.wait()
    else:
        raise NotImplementedError
