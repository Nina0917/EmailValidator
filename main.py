from flask import Flask

app = Flask(__name__)

# flask --app main run
@app.route('/')
def hello():
    return 'Hello, World!'