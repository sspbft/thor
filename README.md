# Thor
[![Build status](https://travis-ci.org/practicalbft/thor.svg?branch=master)](https://travis-ci.org/travis-ci/travis-web)

Service that manages a PracticalBFT application running locally on the same node.

## Set up
First, make sure that you have [Python 3.5](https://www.python.org/downloads/), [pip3.5](https://pip.pypa.io/en/stable/installing/) and [virtualenv](https://pypi.org/project/virtualenv/) installed. Then, follow the commands below.

```
git clone https://github.com/practicalbft/thor.git && cd thor
virtualenv --python=$(which python3.5) ./env && source ./env/bin/activate
pip3.5 install -r requirements.txt
```

Note, if you're having problems with pip, one (or both) of the following commands might help.
```
pip install --upgrade pip
curl https://bootstrap.pypa.io/get-pip.py | python3
```

The code base is linted using [pep8](https://pypi.org/project/pep8/), so make sure to lint the code using this tool before pushing any code.

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
python thor.py -n 5 -f 1 local
```

Make sure to edit `conf/default.ini` to contain the appropriate values or supply them as options through the CLI. 