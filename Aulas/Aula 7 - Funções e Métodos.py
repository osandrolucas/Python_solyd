def soma(n1, n2):
    resp = n1 + n2
    return resp

def imprime_oi(qtd):
    print('Oi ' * qtd)

def tem_sete_itens(argumento):
    if len(argumento) == 7:
        return True
    else:
        return False

print(soma(1,2))
imprime_oi(5)
sete = {1,2,3,4,5,6,7}
print('Posso passar qualquer coleção para a função e ela entenderá.')
if tem_sete_itens(sete):
    print('{} tem 7 itens.'.format(sete))