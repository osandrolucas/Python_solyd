print('''Para ler um arquivo, temos as seguintes opções:'
      Por exemplo --> open('arquivo.txt')
      Observação: Quando não passamos o segundo argumento, assume o r.
      
      Para criar um arquivo --> open('arquivo.txt', 'w')
      Observação: O w faz com que caso não existe o arquivo com o nome, ele é criado. Caso exista, ele sobrescreve.
      Exemplo: arquivo.write('E ai pessoal, beleza? ')
      
      
      Para leitura e escrita --> open('arquivo.txt', 'r+')
      Observação: r de leitura e + para escrita
      
      Para ler um arquivo e acrescentar texto nele --> open('arquivo.txt', 'a')
      Observação: Com o 'a' ele abre o arquivo e acrescenta texto
      
      Para abrir arquivos que não são de texto, usamos o b.
      Exemplo: 
      arq = open('Jellyfish.jpg', 'rb') 
      Observação: Nesse caso, lendo o arquivo somente. Para escrever é outra história.
      
      ''')

#arquivo = open('arquivo.txt', 'w')
#type(print(arquivo))

#arquivo.write('E ai pessoal, beleza? ')

#print(arquivo.read())

#arq = open('Jellyfish.jpg', 'rb')

#print(arq.read())
