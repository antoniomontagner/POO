sex='s'
while True:
	sexo=input('Digite o sexo [F/M]:').upper()
	if sexo == ('F') or sexo == ('M'):
		sex=sexo
		break
if sex==("F"):
	print("Feminino")
else:
	print("Masculino")