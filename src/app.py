from flask import Flask, jsonify
import datetime, socket



app = Flask(__name__)


# '/api/v1/details'

@app.route('/api/v1/details')
def get_details():
    return jsonify({
       'message': 'Details endpoint',
       'hostname': socket.gethostname(),
       'timestamp': datetime.datetime.now().strftime('%I:%M:%S%p on %B %d, %Y')
    })

# '/api/v1/healthz'

@app.route('/api/v1/healthz')
def health():
    return jsonify({
       'status': 'up',
       'response': '200 success',
       'timestamp': datetime.datetime.now().strftime('%I:%M:%S%p on %B %d, %Y')
    })

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)    


