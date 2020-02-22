#-*- coding: utf-8 -*-
# Programa para ler a data de nascimento

print("Digite seu ano de nascimento:")
ano=int(input("Ano:"))
maior_de_idade=ano+18
tempo_restante=(maior_de_idade)-(2019)
tempo_atrasado=tempo_restante*(-1)
print("Ano que faz 18 anos de idade:",maior_de_idade)
if(ano==2001):
	print("Está no ano de se alistar no serviço militar.")
elif(ano>2001):
	print("Ainda não está no ano de se alistar no serviço militar.")
	print("Falta",tempo_restante ,"ano(s) para se alistar.")
elif(ano<2001):
	print("Já passou do tempo de se alistar no serviço militar.")
	print("Passou",tempo_atrasado ,"ano(s) do praso de alistamento.")
