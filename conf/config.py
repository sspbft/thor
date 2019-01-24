
from configparser import ConfigParser
import io

DEFAULT_CONF_PATH = "conf/default.ini"
CUSTOM_CONF_PATH = "conf/custom.ini"

config = ConfigParser()
if io.file_exists(CUSTOM_CONF_PATH):
    config.read(CUSTOM_CONF_PATH)
else:
    config.read(DEFAULT_CONF_PATH)

def get_app_path():
    return config.get("app", "path")

def set_app_path(p):
    return config.set("app", "path", p)

def get_hosts_path():
    return config.get("app", "hosts_path")

def get_entrypoint():
    return config.get("app", "entrypoint")

def set_entrypoint(e):
    config.set("app", "entrypoint", e)

def get_node_count():
    return config.getint("system", "n")

def set_node_count(n):
    config.set("system", "n", str(n))

def get_byzantine_count():
    return config.getint("system", "f")

def set_byzantine_count(f):
    config.set("system", "f", str(f))
