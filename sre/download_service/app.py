# flask_web/app.py

import os

from urllib.request import urlretrieve

from flask import (
    Flask,
    jsonify,
    request,
    Response,
    send_file
)

DEBUG = os.environ.get("DEBUG")
DUMMY_APP_HOST = os.environ.get("DUMMY_APP_SERVICE_HOST")
DUMMY_APP_PORT = os.environ.get("DUMMY_APP_SERVICE_PORT")

app = Flask(__name__)


@app.route('/')
def main():
    '''Main endpoint'''

    result = '''
Welcome to the Random Download Service. 

These are the available endpoints.

/       -  This documentation
/<int>  -  Download an file according the number
/health -  Health check endpoint

# Docs

## /<int>

Returns a file randonly according the value it was passed. 
The value must be an integer following the rule 1 < n < 10.

The file comes from economic dummy-pdf-or-png service and mime-type of files should application/pdf or image/png.

Example: 
    $ curl http://localhost:5000/5

## /health

Health check endpoint.

# Extra Info

- All endpoints accepts HTTP method GET only.
- /int endpoin accepts only integer numbers.
'''
    return Response(result, mimetype='text/plain')


@app.route('/<int:number>')
def download(number):
    '''Download random file endpoint.'''

    fp, request = urlretrieve(f"http://{DUMMY_APP_HOST}:{DUMMY_APP_PORT}")

    #app.logger.info(f'{{"function": "ackermann", "values": [{number}, {number_n}], "elapsed": {time.elapsed}}}')

    return send_file(
        fp,
        mimetype=request.get_content_type()
    )

@app.route('/metrics')
def metrics():
    '''Metrics endpoint for Prometheus.'''

    metrics = {
        "status": helthcheck()["status"],
        "some_metric": 123
    }

    return metrics


@app.route('/health')
def helthcheck():
    '''Health check endpoint.'''

    return {"status": "ok"}


if __name__ == '__main__':
    app.run(debug=DEBUG)
