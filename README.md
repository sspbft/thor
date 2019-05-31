# Thor
[![Build status](https://travis-ci.org/sspbft/thor.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)

Service that manages a SSPBFT application running locally on the same node.

## Set up
First, make sure that you have [Python 3.7](https://www.python.org/downloads/) installed. Then, follow the commands below.

```
git clone https://github.com/sspbft/thor.git && cd thor
python3.7 -m venv env
source env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
mkdir logs
```

The code base is linted using [flake8](https://pypi.org/project/flake8/) with [pydocstyle](https://github.com/PyCQA/pydocstyle), so make sure to lint the code by running `flake8` before pushing any code.

## Usage
Thor is used as a CLI with a set of arguments that can be seen below.

```
usage: thor.py [-h] [-d] [-n NODES] [-f FAULTY] [-p PATH] [-e ENTRYPOINT] [-m]
               [-i ID] [-lp LOGPATH] [-rs RUNSLEEP] [-nss] [-ss] [-s SCALE]
               [-c CLIENTS] [-pf]
               mode

positional arguments:
  mode                  either [local] or [planetlab]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           all output to current shell
  -n NODES, --nodes NODES
                        total number of nodes
  -f FAULTY, --faulty FAULTY
                        number of byzantine nodes
  -p PATH, --path PATH  absolute path to app to run
  -e ENTRYPOINT, --entrypoint ENTRYPOINT
                        start script for app
  -m, --metrics         start heimdall metrics
  -i ID, --id ID        id of the current node
  -lp LOGPATH, --logpath LOGPATH
                        where to write app log
  -rs RUNSLEEP, --runsleep RUNSLEEP
                        s to sleep in module.run
  -nss, --non-selfstab  run without self-stabilization
  -ss, --start-state    tell app that it should load start_state.json in conf/
  -s SCALE, --scale SCALE
                        scale instances on this node
  -c CLIENTS, --clients CLIENTS
                        number of clients
  -pf, --profiling      run app with profiling

```

Example launch of a local environment with specified number of nodes and faulty nodes along with Heimdall metrics:
```
python3.7 thor.py -n 6 -f 1 -m local
```

Make sure to edit `conf/default.ini` or add a custom file at `conf/custom.ini` and add appropriate values.
