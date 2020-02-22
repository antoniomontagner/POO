"""p1=int(input("populacao pais 1: "))
p2=int(input("populacao pais 2: "))
anos=0
while p1<p2:
	p1=(p1*0.03)+p1
	p2=(p2*0.015)+p2
	anos+=1
print(f"anos para pais 1 passar pais 2 sara de {anos} na taxa de 0.03 e 0.015 % ao ano. ")
"""

def pop(p,pp):
	p=p
	pp=pp
	anos=0
	while p<pp:
		p=(p*0.03)+p
		pp=(pp*0.015)+pp
		anos+=1
	return anos
p1=80000
p2=200000
anos=pop(p1,p2)
print(f"anos para pais 1 passar pais 2 sara de {anos} na taxa de 0.03 e 0.015 % ao ano. ")
