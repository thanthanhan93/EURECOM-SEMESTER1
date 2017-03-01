import socket

HOST = 'localhost';
PORT = 9999;

ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_socket.connect(('localhost', 9999))

data = ser_socket.recv(1024)
#print data;
data = ser_socket.recv(1024)
#print data;

ser_socket.send('thanthanhan' + '\n')
data = ser_socket.recv(1024)
#print data;
ser_socket.sendall('3037065bbb7bd262e27b24dca52c0cf7\n')

data = ser_socket.recv(1024)
ser_socket.send('5000\n')
n_max=10000;n_min=0;n_cur=5000;
while True:
    data = ser_socket.recv(1024)
    #print '{0}: {1}'.format(n_cur,data)
    if "BRAVO" in data:
        break
    if "bigger" in data:
        n_min=n_cur
    if "smaller" in data:
        n_max=n_cur 
    n_cur=int((n_max-n_min)/2+n_min)
    ser_socket.send(str(n_cur) + '\n')

while True:
    data = ser_socket.recv(1024)
    print data
    data = raw_input ( "INPUT:" )
    ser_socket.send(data + '\n')


