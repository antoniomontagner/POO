
"""n=int(input("numero: "))
s=n
for i in range(4):
	n2=int(input("numero: "))
	s+=n2
	if n2>n:
		n=n2
m=s/5
print(f"maior numero é {n}, soma {s} e media {m}.")
"""
"""def num(x):
	s=x
	for i in range(4):
		n2=int(input("numero: "))
		if n2>s:
			s=n2
	
	return s
n=int(input("numero: "))
conta=num(n)
print(f"maior numero é {conta}")
"""

def num(x):
	s=x
	soma=0
	for i in range(4):
		n2=int(input("numero: "))
		soma+=n2
		if n2>s:
			s=n2
	media=soma/5
	
	return s,soma,media
n=int(input("numero: "))
conta=num(n)
print(f"maior numero é {s} soma é {soma} e media {media}")