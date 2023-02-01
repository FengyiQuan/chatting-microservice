import logging
# import flask
from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import flask_login
from .models.User import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

socketio = SocketIO(app)

users = {'test': {'password': 'test'}}


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')


@app.route('/user/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        print(True)
        return render_template('user/login.html')

    email = request.form['username']
    if email in users and request.form['password'] == users[email]['password']:
        # print(True)
        user = User()
        # print(False)
        user.id = email
        flask_login.login_user(user)
        return redirect(url_for('protected'))
    else:
        print(True)
        return 'Bad login'


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email

    return user


@app.route('/protected')
@flask_login.login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized', 401


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
    # application on Google App Engine. See entrypoint in app.yaml.
    socketio.run(app)
    # app.run(host='127.0.0.1', port=8080, debug=True)
