# thor
Service that manages an application service running on the same node.

## Set up
```
git clone https://github.com/practicalbft/thor.git && cd thor
virtualenv --python=<absolute_path_to_python3.5_binary> ./env
source ./env/bin/activate
pip install -r reqs.txt
```

Note, if you're having problems with pip, one (or both) of the following commands might help.
```
pip install --upgrade pip
curl https://bootstrap.pypa.io/get-pip.py | python3
```

Simply run `FLASK_APP=api/api.py flask run` and the server can be found on [localhost:5000](http://localhost:5000)!