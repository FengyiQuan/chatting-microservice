import logging
# import flask
from datetime import datetime

from flask import Flask, flash, render_template, request, redirect, url_for
# from flask_login import logout_user, login_required, current_user, LoginManager, login_user
# from flask_socketio import SocketIO, join_room, leave_room
# from pymongo.errors import DuplicateKeyError

# from dao.db import save_user, get_user_by_username, get_user_by_id

# from is_safe_url import is_safe_url

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'
room = 'general'  # only one room for now


@app.route('/')
def index():
    """Return a friendly HTTP greeting."""
    return render_template('index.html')


# @app.route('/user/login', methods=['GET', 'POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#
#     if request.method == 'GET':
#         return render_template('auth/login.html')
#     else:
#         username = request.form['username']
#         password = request.form['password']
#         user = get_user_by_username(username)
#         if user and user.check_password(password):
#             login_user(user)
#             # print('login successful')
#             next = request.args.get('next')
#             # if True or not is_safe_url(next):
#             #     return abort(400)
#             return redirect(next or url_for('index'))
#         else:
#             flash('Invalid username or password', 'danger')
#             return redirect(url_for('login'))
#
#
# @app.route('/user/register', methods=['GET', 'POST'])
# def signup():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#
#     if request.method == 'GET':
#         return render_template('auth/signup.html')
#     else:
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']
#         password2 = request.form['password2']
#         user = get_user_by_username(username)
#         if password != password2:
#             flash('Passwords do not match', 'danger')
#             return redirect(url_for('signup'))
#         if user:
#             flash('User already exists', 'danger')
#             return redirect(url_for('signup'))
#         else:
#             try:
#                 save_user(username, email, password)
#                 flash('Please sign in', 'success')
#                 return redirect(url_for('login'))
#             except DuplicateKeyError:
#                 flash('User already exists', 'danger')
#                 return redirect(url_for('signup'))
#
#
# @app.route("/logout", methods=['POST'])
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('index'))


# @app.route('/rooms/<room_id>/', methods=['GET'])
# # @login_required
# def view_room(room_id):
#     # room = get_room(room_id)
#     # if room:  # and is_room_member(room_id, current_user.username):
#     # room_members = get_room_members(room_id)
#     # messages = get_messages(room_id)
#     return render_template('chatroom/view_room.html', room=room)
    # room_members=room_members)
    # messages=messages)
    # else:
    #     return "Room not found", 404


# socketio events
# @socketio.on('send_message')
# def handle_send_message_event(data):
#     app.logger.info("{} has sent message to the room {}: {}".format(data['username'],
#                                                                     data['room'],
#                                                                     data['message']))
#     print("{} has sent message to the room {}: {}".format(data['username'],
#                                                           data['room'],
#                                                           data['message']))
#     data['created_at'] = datetime.now().strftime("%d %b, %H:%M")
#     data['room'] = room
#     # save_message(data['room'], data['message'], data['username'])
#     socketio.emit('receive_message', data, room=data['room'])
#
#
# @socketio.on('join_room')
# def handle_join_room_event(data):
#     app.logger.info("{} has joined the room {}".format(data['username'], data['room']))
#
#     data['room'] = room
#     print("{} has joined the room {}".format(data['username'], data['room']))
#     join_room(data['room'])
#     socketio.emit('join_room_announcement', data, room=data['room'])
#
#
# @socketio.on('leave_room')
# def handle_leave_room_event(data):
#     app.logger.info("{} has left the room {}".format(data['username'], data['room']))
#     data['room'] = room
#     print("{} has left the room {}".format(data['username'], data['room']))
#     leave_room(data['room'])
#     socketio.emit('leave_room_announcement', data, room=data['room'])


# @login_manager.unauthorized_handler
# def unauthorized_handler():
#     return 'Unauthorized', 401


# @app.errorhandler(500)
# def server_error(e):
#     logging.exception('An error occurred during a request.')
#     return """
#     An internal error occurred: <pre>{}</pre>
#     See logs for full stacktrace.
#     """.format(e), 500


# @login_manager.user_loader
# def load_user(user_id):
#     # print(user_id)
#     user = get_user_by_id(user_id)
#     # print(user)
#     return user


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8080, log_level="info")

# if __name__=='__main__':
#     app.run(host="0.0.0.0", port=5000)
