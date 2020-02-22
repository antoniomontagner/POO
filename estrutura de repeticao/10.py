def xsss(s,m):
	x=0
	y=1
	for i in range (s,m+1):
		x+=i
		y*=i
	return x,y
n1=int(input("numero 1: "))
n2=int(input("numero 2: "))
calc=xsss(n1,n2)
print(calc)
