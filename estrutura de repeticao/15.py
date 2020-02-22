def jaca():
	n0=0
	n1=1
	nn=0
	tn=int(input("numero: "))
	for i in range(tn):
		n0=n1
		n1=nn

		nn=n1+n0
		print(nn)
x=jaca()