from flask import Flask
import tushare as ts
from flask_socketio import SocketIO, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)


@app.route('/')
def hello():
    return 'Hello world!'


@app.route('/blotter/<symbol>')
def blotterDetail(symbol=None):
    print('symbole = ', symbol)
    df = ts.get_realtime_quotes(symbol)
    json = df.loc[0].to_json()
    print(json)
    return json


@app.route('/market')
def market():
    print('fetching market...')
    df = ts.get_today_all()
    print('df = ', df)
    json = df.to_json(orient='records')
    print(json)
    return json


@socketio.on('blotter-detail')
def blotterDetailSocket(symbol=None):
    emit('blotter-detail-response', {'data': 'got it'})


@socketio.on('send_message')
def handle_source(json_data):
    text = json_data['message'].encode('ascii', 'ignore')
    socketio.emit('echo', {'echo': 'Server Says: ' + text})


if __name__ == '__main__':
    # app.run(host='0.0.0.0')
    socketio.run(app)
