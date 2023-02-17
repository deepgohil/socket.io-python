import socketio
import datetime
import base64

sio = socketio.Client()


with open("i.jpg", "rb") as f:
    lines = base64.b64encode(f.read())

# //////////////////////////send text file over socket
@sio.event
def connect():
    print('connection established')
    sio.emit('test', lines)
            # loopvar=False
        # datatoemit=int(input("ENter data to emit"))
        # x = str(datetime.datetime.now())
        

# @sio.event
# def connect():
#     print('connection established')
#     with open("i.jpg", "rb") as image2string:
#         converted_string = base64.b64encode(image2string.read())
#         sio.emit('test', {'data': converted_string})


@sio.event
def message(data):
    print('message received with ', data)
    # sio.emit('my response', {'response': 'my response'})
    # sio.emit('my message', {'foo': 'bar'})
   
@sio.event
def disconnect():
    print('disconnected from server')

sio.connect('http://localhost:5000')
sio.wait()