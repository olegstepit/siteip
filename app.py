from flask import Flask, request, jsonify
import socket
import requests

app = Flask(__name__)

@app.route('/')
def get_ip_addresses():
    internal_ip = socket.gethostbyname(socket.gethostname())
    external_ip = requests.get('https://api64.ipify.org?format=json').json()['ip']

    data = {
        'internal_ip': internal_ip,
        'external_ip': external_ip,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
