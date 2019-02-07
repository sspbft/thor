"""Various helper methods related to subprocess management."""
import psutil
import logging

pids = []
logger = logging.getLogger(__name__)


def kill(pid):
    """Kills a subprocess given by its PID and its subprocesses as well."""
    process = psutil.Process(pid)
    for proc in process.children(recursive=True):
        proc.kill()
    process.kill()


def kill_all_subprocesses():
    """Kills all running subprocesses and terminates program if exit = True."""
    for pid in pids:
        logger.info("Killing subprocess with pid {}".format(pid))
        kill(pid)
    logger.info("Killed all subprocesses")


def add_subprocess_pid(pid):
    """Adds PID of subprocess to list of running subprocesses."""
    pids.append(pid)
