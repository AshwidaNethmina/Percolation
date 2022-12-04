import random

def generater():
	none_probability = 0.1
	if random.random() < none_probability:
		return None
	else:
		return random.randint(10,99)


#list 1
list1 = []
for i in range (0,8):
	list1.append(generater())

#list 2
list2 = []
for i in range (0,8):
	list2.append(generater())
	
#list 3
list3 = []
for i in range (0,8):
	list3.append(generater())
	
#list 4
list4 = []
for i in range (0,8):
	list4.append(generater())
	
#list 5
list5 = []
for i in range (0,8):
	list5.append(generater())
	
#list 6
list6 = []
for i in range (0,8):
	list6.append(generater())
	
#list 7
list7 = []
for i in range (0,8):
	list7.append(generater())
	
#list 8
list8 = []
for i in range (0,8):
	list8.append(generater())
	
#list 9
list9 = []
for i in range (0,8):
	list9.append(generater())
	
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)
print(list6)
print(list7)
print(list8)
print(list9)

for i in range (0,8):
	if(list1[i] == None or list2[i] == None or list3[i] == None or list4[i] == None or list5[i] == None or list6[i] == None or list7[i] == None or list8[i] == None or list9[i] == None ):
		print("No",end=" ")
	else:
		print("Ok",end=" ")
		
		