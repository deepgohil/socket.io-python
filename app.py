import eventlet
import socketio

sio = socketio.Server()

app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

# @sio.on('Hello', namespace='/chat')
# def my_custom_event(sid, data):
#     print(sid)
#     print(data)

# @sio.event
# def my_message(sid, data):
#     print('message ', data)

# @sio.on('cMsg',namespace='/chat')
# def test(sid,data):
#     print('disconnect ', data)

@sio.event(namespace='/chat')
def connect(sid, environ):
    print('connect ', sid)

# @sio.event
# def disconnect(sid):
#     print('disconnect ', sid)

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)