# thor
Service that manages an application service running on the same node.

## Set up
First, make sure that you have [Python 3.5](https://www.python.org/downloads/), [pip3.5](https://pip.pypa.io/en/stable/installing/) and [virtualenv](https://pypi.org/project/virtualenv/) installed. Then, follow the commands below.

```
git clone https://github.com/practicalbft/thor.git && cd thor
virtualenv --python=$(which python3.5) ./env && source ./env/bin/activate
pip3.5 install -r reqs.txt
```

Note, if you're having problems with pip, one (or both) of the following commands might help.
```
pip install --upgrade pip
curl https://bootstrap.pypa.io/get-pip.py | python3
```

Now you can simple run `FLASK_APP=api/api.py flask run` and the server can be found on [localhost:5000](http://localhost:5000)!