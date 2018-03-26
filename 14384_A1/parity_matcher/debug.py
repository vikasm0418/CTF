import sys
import socket
import time

hostname = sys.argv[1]
port = int(sys.argv[2])

def netcat(hn,p):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((hn,p))
	
	res = ""
	sock.recv(1024)
	sock.sendall('1\n')
	for i in range(0,600):
		data = sock.recv(1024)
		print data
		if(data[1:10].count('1')%2==1):
			print('yes')
			print(data[1:9])
			sock.sendall('1\n')
			res += data[1:9]
		else:
			print('no')
			print(data[1:9])
			sock.sendall('0\n')
	print res

	sock.close()


netcat(hostname,port)	
