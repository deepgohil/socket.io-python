import eventlet
import socketio
import base64

sio = socketio.Server()
app = socketio.WSGIApp(sio, static_files={
    '/': {'content_type': 'text/html', 'filename': 'index.html'}
})

@sio.event
def connect(sid, environ):
    print('connect ', sid)

# //////////////////////////for text 
@sio.event
def test(sid, data):
     # handle the message
    # print(sid)
    decodeit = open('hello_level.jpeg', 'wb')
    decodeit.write(base64.b64decode((data)))
    decodeit.close()
    print(type(data))
    # sio.emit("message",data,to=sid)


# //////////////////////////////////for image
# @sio.event
# def test(sid, data):
#      # handle the message
#     print(sid)
#     print(data)
#     decodeit = open('img.jpeg', 'wb')
#     decodeit.write(base64.b64decode((data)))
#     decodeit.close()


@sio.event
def disconnect(sid):
    print('disconnect ', sid)




if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('', 5000)), app)