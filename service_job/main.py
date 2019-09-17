import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/job/message')
def job():
    response = { 'message': "Hello from the Job microservice" }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)