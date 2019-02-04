# Thor
[![Build status](https://travis-ci.org/practicalbft/thor.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)

Service that manages a PracticalBFT application running locally on the same node.

## Set up
First, make sure that you have [Python 3.7](https://www.python.org/downloads/) installed. Then, follow the commands below.

```
git clone https://github.com/practicalbft/thor.git && cd thor
python3.7 -m venv env
pip install --upgrade pip
pip install -r requirements.txt
```

The code base is linted using [flake8](https://pypi.org/project/flake8/) with [pydocstyle](https://github.com/PyCQA/pydocstyle), so make sure to lint the code by running `flake8` before pushing any code.

## Usage
Thor is used as a CLI with a set of arguments that can be seen below.

```
usage: thor.py [-h] [-n NODES] [-f FAULTY] [-p PATH] [-e ENTRYPOINT] [-m] mode

positional arguments:
  mode                  either [local] or [planetlab]

optional arguments:
  -h, --help            show this help message and exit
  -n NODES, --nodes NODES
                        total number of nodes
  -f FAULTY, --faulty FAULTY
                        number of byzantine nodes
  -p PATH, --path PATH  absolute path to app to run
  -e ENTRYPOINT, --entrypoint ENTRYPOINT
                        start script for app
  -m, --metrics         start heimdall metrics
```

Example launch of a local environment with specified number of nodes and faulty nodes:
```
python3.7 thor.py -n 5 -f 1 local
```

Make sure to edit `conf/default.ini` to contain the appropriate values or supply them as options through the CLI. 