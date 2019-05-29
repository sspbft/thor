"""Config module."""
from configparser import ConfigParser
from helpers import io

DEFAULT_CONF_PATH = "conf/default.ini"
CUSTOM_CONF_PATH = "conf/custom.ini"

config = ConfigParser()
if io.exists(CUSTOM_CONF_PATH):
    config.read(CUSTOM_CONF_PATH)
else:
    config.read(DEFAULT_CONF_PATH)


def get_app_path():
    """Returns the configured absolute path to the app root."""
    return config.get("app", "path")


def set_app_path(p):
    """Sets the absolute path to the app root."""
    return config.set("app", "path", p)


def get_hosts_path():
    """Returns the absolute path to the file with all hosts in the system."""
    return config.get("app", "hosts_path")


def get_entrypoint():
    """Retuns the configured entrypoint for the app to be launched."""
    return config.get("app", "entrypoint")


def set_entrypoint(e):
    """Sets the entrypoint to be used when launching an app through Thor."""
    config.set("app", "entrypoint", e)


def get_node_count():
    """Returns the configured total number of nodes."""
    return config.getint("system", "n")


def set_node_count(n):
    """Sets the number of total nodes to n."""
    config.set("system", "n", str(n))


def get_byzantine_count():
    """Returns the configured number of Byzanine nodes."""
    return config.getint("system", "f")


def set_byzantine_count(f):
    """Sets the number of Byzantine nodes to f."""
    config.set("system", "f", str(f))


def get_log_path():
    """Returns the absolute path to the logs directory for Thor."""
    return config.get("etc", "log_path")


def get_heimdall_root():
    """Returns the absolute path to the Heimdall project root."""
    return config.get("etc", "heimdall_root")
