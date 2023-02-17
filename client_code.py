import socketio
import datetime
import base64

sio = socketio.Client()


# //////////////////////////send text file over socket
# @sio.event
# def connect():
#     print('connection established')
#     loopvar=True
#     while(loopvar):
#         with open('readme.txt') as f:
#             lines = str(f.readlines())
#             loopvar=False
#         # datatoemit=int(input("ENter data to emit"))
#         # x = str(datetime.datetime.now())
#         sio.emit('test', {'data': lines})




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