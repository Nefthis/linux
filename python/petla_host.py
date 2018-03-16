import os


for server in open('server_list.txt'):
	os.system('host -tns '  + server) 

