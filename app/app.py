import os
import sys
from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"message": "Shalom, " + request.remote_addr + ", You Are Using Port: " + os.environ["FLASK_PORT"] })

if __name__ == '__main__':
    flask_port = None
    try:
        flask_port = os.environ["FLASK_PORT"]
    except KeyError:
        print("Expected FLASK_PORT to be set. Exiting.")
        sys.exit(1)
    app.run(debug=True, host='0.0.0.0', port=flask_port)
