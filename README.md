## Pythone 3.5+ 
```
pip3 install chatterbot
pip3 install flask flask-jsonpify flask-sqlalchemy flask-restful flask_cors
```
## Local demo with back-end only, train with different languages, after training the database will be shared for any language inputs.
```
python3 mandarin-demo.py
python3 english-demo.py
python3 cantonese-demo.py
```
## Api back-end enable
```
python3 english-api.py 
```
## Sample API for english conversation
```
http://localhost:5080/conversation

  {
    "user": "你边度唔舒服?"
  }
  
```