#    1
#   232
#  34543...
k=4
for i in range(1,6):
	print(" "*k,end ="")
	y=(2*i)-1#this is the algorithm of my program,slightly complicated than very genious animeshs algorithm
	for j in range(i,y+1):
		print(j,end="")
	for j in range(y-1,i-1,-1):
		print(j,end="")
	print()
	k=k-1
#rem i could not complete this program in time due to variable name conflict, in 1st try,i miscoded every k variable as j this caused an error