import datetime

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def root():
    return jsonify({'greeting': 'Hello from default service'})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)