import socket
import pickle
import re
import datetime

HOST = 'localhost';
PORT = 9999;

ser_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_socket.connect(('localhost', 9999))

def num_detect(num):
    if(num == 1221115):
        return 1
    if(num == 5215117):
        return 2
    if(num == 5215125):
        return 3
    if(num == 1227111):
        return 4
    if(num == 7115125):
        return 5
    if(num == 5216225):
        return 6
    if(num == 7211111):
        return 7
    if(num == 5225225):
        return 8
    if(num == 5226125):
        return 9
    if(num == 3233323):
        return 0

def count_character(text):
    return text.count("#");
    
def number_array(text):
    height = text.split("\n")
    height = height[:len(height)-3]
    len(height[0])
    num_rowcount = [0,0,0]
    for i in range(0,len(height)):
        #print 'r{1}: {0}'.format(height[i],i)
        num_rowcount[0]=num_rowcount[0]*10+count_character(height[i][:7])
        num_rowcount[1]=num_rowcount[1]*10+count_character(height[i][8:23])
        num_rowcount[2]=num_rowcount[2]*10+count_character(height[i][24:])
    #print num_rowcount;
    result = 0
    for i in range(0,len(num_rowcount)):
        result = result*10+num_detect(num_rowcount[i])
    return result

def question3(text):
    lines = text.split("\n")
    lines = lines[1:9];
    date = '\n'.join(lines)
    date = pickle.loads(date)
    #print type(date)
    #print date
    return date.microsecond

def month(text):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months.index(text)+1

def question4(text):
    date_match = re.findall(r'\d{2} \w{3} \d{2}',text)[0]
    #print date_match[7:8], date_match[3:5], date_match[0:2]
    date = datetime.date(int('20'+date_match[7:9]),month(date_match[3:6]),int(date_match[0:2]))
    return date.strftime('%A');

def getsecretkey(text):
    lines = text.split("\n")
    return lines[len(lines)-3]

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

data = ser_socket.recv(1024)
print data
data = str(number_array(data))
print data
ser_socket.send(data + '\n')

data = ser_socket.recv(1024)
data = ser_socket.recv(1024)
print data
data = question3(data);
print data
ser_socket.send(str(data)+ '\n')


data = ser_socket.recv(1024)
data = ser_socket.recv(1024)
print data
data = question4(data)
print data
ser_socket.send(str(data)+ '\n')

data = ser_socket.recv(1024)
print data
data = getsecretkey(data)
print data

