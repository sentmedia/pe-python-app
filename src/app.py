from flask import Flask

app = Flask(__name__)

@app.route('/api/v1/details')
def get_details():
    return 'My Flask app says Hello World!'

if __name__ == '__main__':
    app.run()    

# '/api/v1/details'
# '/api/v1/healthz'