qnt_pessoas = int(input('Quantidade de pessoas: '))
sum_idade = 0 
for i in range(qnt_pessoas):
    idade = int(input('Idade: ')) 
    sum_idade += idade 
    if 0 < sum_idade <= 25:
        print('jovem')
    elif 25 < sum_idade <= 60: 
        print('adulto')
    else: 
        print('idoso')
media=sum_idade/qnt_pessoas
if 0 < media <= 25:
    print('turma jovem')
elif 25 < media <= 60: 
    print('turma adulta')
else:
    print('turma idosa')