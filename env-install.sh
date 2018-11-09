apt-get install -y build-essential libssl-dev libffi-dev python-dev python-tk curl
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
pip install flask flask-jsonpify flask-sqlalchemy flask-restful

