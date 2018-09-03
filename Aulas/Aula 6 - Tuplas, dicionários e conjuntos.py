#Exemplo de lista
print('## Exemplo de Lista ## ')
minha_lista = ['Sandro', 'Lucas']
print(minha_lista)
print(type(minha_lista))
print('\nAlgumas caracteristicas de uma lista...\n1. Está sempre ordenada\n2. É mútavel\n3. Pode incluir/alterar/Remover Objetos\n4. Apenas um elemento em cada posção\n5. Infinita')


print('\n## Exemplo de Tupla ## ')
minha_tupla = ('Sandro', 'Lucas')
print(minha_tupla)
print(type(minha_tupla))
print('\nAlgumas caracteristicas de uma Tupla...\n1. Não é mutável, objetos não podem ser removidos ou adicionados\n2. É possivel alterar\n3. Tem índice, assim como a lista\n4. Quando for substituir algo, tem que substituir ela toda\n5. É utilizada para coisas mais estáveis\n6. Bastante eficiente em buscas')


print('\n## Exemplo de Dicionário ## ')
meu_dicionario = {'nome': 'Sandro Lucas', 'idade': 23} #Key and Value
print(meu_dicionario)
print(type(meu_dicionario))
print('\nAlgumas caracteristicas de um Dicionário...\n1. Tem uma chave e um valor\n2. Semelhante ao dicionário real\n3. Parecido com Json\n4. Conhecido em HashMap ou Hash Table ou Dict\n5. É dinâmico')

print('\n## Exemplo de Conjunto ## ')
meu_conjunto = {'Sandro', 'Lucas'}
print(meu_conjunto)
print(type(meu_conjunto))
print('\nAlgumas caracteristicas de um Conjunto...\n1. Parecido com uma lista misturada com dicionário\n2. Não tem uma chave e valor, tem só o valor\n3. Não existe itens repetidos, se adicionar nada acontece\n4. Não é ordenado\n5. É dinâmico\n6. Conhecido como set no Python\n7. Bastante eficiente em buscas')

print('\n### Lidando um pouco com Tuplas ###')

print('\nÉ possivel descobrir se um Objeto está dentro de qualquer um dessas coleções, só usar o IN...')
print('Por exemplo --> Lucas está dentro da Tupla?')
if 'Lucas' in minha_tupla:
    print('Sim, está na Tupla!')
print('Por exemplo --> Ronaldinho está dentro da Tupla?')
if 'Ronaldinho' in minha_tupla:
    print('Sim, está na Tupla!')
else:
    print('Não, ele não está!')

print('\n### Lidando um pouco com Dicionários ###')

print('\nPegando valor de uma chave no Dicionário...')
print('Qual o valor da chave "nome" no meu dicionário?')
print(meu_dicionario['nome'])
print('\nQuantos elementos tem no meu dicionário? {}'.format(len(meu_dicionario)))

print('Sandro Lucas está no dicionário? ')
if 'Sandro Lucas' in meu_dicionario.values():
    print('Existe algum valor "Sandro Lucas" no dicionário!')
else:
    'Sandro Lucas não está no dicionário!'

print('\nQuais os valores estão no meu dicionário?')
for i in meu_dicionario.values():
    print(i)

print('\nQuais as chaves estão no meu dicionário?')
for i in meu_dicionario.keys():
    print(i)

print('Mudando um valor dentro de uma chave no dicionário... De: "Sandro Lucas" - Para: "Sandiely"')
meu_dicionario['nome'] = 'Sandiely'
print(meu_dicionario)

print('\nAdicionando a chave "endereco" no dicionário e seu valor...')
meu_dicionario['endereco'] = 'Professor Luis Carlos Jardim, 280'
print(meu_dicionario)

print('\nAdicionando a chave "telefone" no dicionário e seu valor...')
meu_dicionario['telefone'] = '9999.9999'
print(meu_dicionario)

print('### Lidando com Conjuntos ###')
print('Existe "Sandro" no conjunto?')
if 'Sandro' in meu_conjunto:
    print('Sim, existe!')
else:
    print('Não!')

print('\nRemovendo "Lucas" do Conjunto')
print('Antes de remover: {}'.format(meu_conjunto))
meu_conjunto.remove('Lucas')
print('Depois de remover: {}'.format(meu_conjunto))

print('Inicializando as coleções...')
print('Para inicializar uma lista --> lista = []')
print('Para inicializar uma tupla --> tupla = ()')
print('Para inicializar um dicionário --> dicionário = {} / dict()')
print('Para inicializar um conjunto --> set()')

print('\nAs possibilidades são infinitas, é possível colocar uma coleção dentro de outra. \nDá para fazer uns negócios "loucos" tipo, uma lista com várias tuplas dentro(4) com diferentes tipos dentro...')
loucura = [(1,2), (3,4), (5,6), ({'joao', 'maria'}, {'sandro'})]
print(loucura)

print('Documentação: https://docs.python.org/3/')