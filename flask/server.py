import logging

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')


@app.route('/newroute/<name>')
def newroute(name):
    """parameter"""
    return "this was passed in: %s" % name


@socketio.on('newMessage')
def handle_message(new_message):
    print('received message: ' + new_message)
    socketio.emit('newMessage', new_message)


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


if __name__ == '__main__':
    # This is used when running locally. Gunicorn is used to run the
    # application on Google App Engine. See entrypoint in flask.yaml.
    socketio.run(app)
    # flask.run(host='127.0.0.1', port=8080, debug=True)