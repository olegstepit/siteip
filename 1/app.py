from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def get_system_info():
    data = {
        'host': request.host,
        'ip': request.remote_addr,
        'user_agent': request.headers.get('User-Agent'),
        'method': request.method,
        'scheme': request.scheme,
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
