# -*- coding: utf-8 -*-
# programa para calcular valor a ser pago por um produto
escreva("Digite o valor total de compra");
escreva("Digite 1, vista ou cheque");
escreva("Digite 2, cartao de credito");
escreva("Digite 3, 2 vezes sem juros");
escreva("Digite 4, 3 vezes 10% de juros");
leia(preço);
se(codigo=1);
escreva("recebe 10% de desconto");
fimse;
escreva("Condição de Pagamento");
leia(preço)
se(codigo=2);
escreva("recebe 5% de desconto");
fimse;
escreva("Condição de Pagamento");
leia(preço);
se(codigo=3);
escreva("Em 2 vezes, preço normal de etiqueta sem juros");
fimse;
escreva("Condição de Pagamento");
leia(preço);
se(codigo=4);
escreva("Em 3 vezes, preço normal de etiqueta mais juros de 10%");

print("Para pagamento em 1x no cartão:2")
print("Para pagamento em 2x no cartão:3")
print("Para pagamento em 3x ou mais no cartão:4")