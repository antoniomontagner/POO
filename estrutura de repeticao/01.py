
"""n=int(input("nota: "))
while 0>n or n>	10:
	n=int(input("digite novamente: "))
print(f"nota é {n}.")

"""

def nota (n):
	n=n
	while 0>n or n>	10:
		n=int(input("digite novamente: "))
	else:
		n=n	
		return n
n1=int(input("nota: "))
nota0=nota(n1)
print(f"nota é {nota0}")