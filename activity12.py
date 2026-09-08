import getpass 

username = 'zai1'
password = 'zairanne0310' 

u = input("Enter username ----> ")
p = getpass.getpass("Enter password ---->")

if username == u and password == p:
 	print("ACCESS GRANTED")
else: 
	print("ACCESS DENIED") 