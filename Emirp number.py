def prime(a):
	c =0
	for i in  range(2,(a//2)+1):
		if a%i == 0:
			c+=1
	return c==0
if __name__== "__main__":
	a= int (input())
	print(prime(a) and prime(int(str(a)[::-1])))