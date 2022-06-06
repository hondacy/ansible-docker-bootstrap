import os
import sys
from flask import Flask
from flask import request
from flask import jsonify
from datetime import date

app = Flask(__name__)

@app.route('/')
def hello_world():
    curr_date = date.today().strftime("%d/%m/%Y")
    return jsonify({"message": ""+ curr_date +" Shalom, " + request.remote_addr + ", You Are Using Port: " + os.environ["FLASK_PORT"] })

if __name__ == '__main__':
    flask_port = None
    try:
        flask_port = os.environ["FLASK_PORT"]
    except KeyError:
        print("Expected FLASK_PORT to be set. Exiting.")
        sys.exit(1)
    app.run(debug=True, host='0.0.0.0', port=flask_port)
