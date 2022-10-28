x=input()
s=0
for i in range(0,len(x)):
	s+=int(x[i])
print(int(x)%s==0)