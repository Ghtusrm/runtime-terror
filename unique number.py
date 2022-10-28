x=input()
s=True
for i in range(0,len(x)):
	if(x[i] in x[0:i]+x[i+1:len(x)]):
		s=False
		break
print(s)