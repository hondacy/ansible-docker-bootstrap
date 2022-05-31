import json
import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return json.dumps({"message": "Shalom there, Using Port: " + os.environ["FLASK_PORT"] })


if __name__ == '__main__':
    flask_port = None
    try:
        flask_port = os.environ["FLASK_PORT"]
    except KeyError:
        print("Expected FLASK_PORT to be set. Exiting.")
        sys.exit(1)
    app.run(debug=True, host='0.0.0.0', port=flask_port)




# @app.get("/value")
# def get_value():
#     return json.dumps({"value": str(r.get('value'))})
# @app.post("/value")
# def set_value():
#     r.set("value", str(request.json['value']))


# if __name__ == '__main__':
#     redis_url = None
#     try:
#         redis_url = os.environ["REDIS_URL"]
#     except KeyError:
#         print("Expected REDIS_URL to be set. Exiting.")
#         sys.exit(1)

#     r = redis.StrictRedis(host=redis_url, port=6379, db=0)
#     app.run(host="0.0.0.0")