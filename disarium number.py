x=input()
s=0
for i in range(0,len(x)):
	s+= int(x[i])**(i+1)
print(s==int(x))