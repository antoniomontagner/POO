def pop(p,pp,t,tt):
	p=p
	pp=pp
	anos=0
	while p<pp:
		p=(p*t)+p
		pp=(pp*tt)+pp
		anos+=1
	return anos

    p1=int(input("populacao pais 1: "))
    p2=int(input("populacao pais 2: "))
    taxa1=float(input("taxa 1: "))
    taxa2=float(input("taxa 2: "))
    anos=pop(p1,p2,taxa1,taxa2)

    print(f"anos para pais 1 passar pais 2 sara de {anos} na taxa de 0.03 e 0.015 % ao ano. ")