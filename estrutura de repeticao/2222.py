n1=int(input("numero 1: "))
n2=int(input("numero 2: "))
s=0
m=1
for i in range (n1,n2):
	s+=i
	m*=i
print(s,m)