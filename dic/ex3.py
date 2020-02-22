from operator import itemgetter
dic={}
for i in range(4):
    j=input("jogador: ")
    dic[f"{j}"]=input("numero: ")
print(dic)

print(sorted(dic.items(), key=itemgetter(1)))

print(sorted(dic.items(), key=itemgetter(0),reverse=True))
maior=''
for i in range(4):
    
