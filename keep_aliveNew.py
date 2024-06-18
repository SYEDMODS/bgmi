from flask import Flask, render_template
from threading import Thread
from gevent.pywsgi import WSGIServer

app = Flask(__name__)
#@app.route('/api', methods=['GET'])
@app.route('/')
def index():
    return "Alive"

#if __name__ == '__main__':
def run():
    # Debug/Development
# app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
#    app.run(host='0.0.0.0',port=8080)
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()

def keep_alive():
    t = Thread(target=run)
    t.start()    
    
    
    
    