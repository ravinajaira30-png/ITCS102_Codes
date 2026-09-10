#Write a python that accepts an integer 

name= input("Input NAME ----> ")
age = int(input("Input AGE ----> "))

if age  >=1 and age <=5:
		print("infant") 
elif age >= 6 and age <=12:
	print("KID")
elif age >=13 and age <=19:
	print("teenager")
elif age >=20 and age <=29:
	 print("early adulthood")
elif age >=30 and age <=48:
	print("adult")
elif age >=49 and age <=59:
	print("advance adult")
elif age >=60 and age <=150:
	print("senior")
else:
	print("invalid")