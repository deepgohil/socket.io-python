import socketio

# sio = socketio.Client()
sioNs = socketio.Client()


@sioNs.on('connect', namespace='/chat')
def on_connect():
    print("I'm connected to the /chat namespace!")
    # sioNs.emit("cMsg",{"hello","12300"},namespace='/chat')




# @sio.event
# def my_message(data):
#     print('message received with ', data)
#     sio.emit('my response', {'response': 'my response'})

# @sio.event
# def disconnect():
#     print('disconnected from server')

# sio.connect('http://localhost:5000')
sioNs.connect('http://localhost:5000', namespaces=['/chat'])
sioNs.wait()