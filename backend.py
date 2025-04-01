#. Estruturas de Controle
#Condicionais
#Comando	O que faz
#if	Executa um bloco de código se a condição for verdadeira.
#elif	Define uma condição alternativa.
#else	Define um bloco de código para quando nenhuma condição for atendida.

#1. Comandos Básicos
#Comando	O que faz
#print()	Exibe uma mensagem na tela.
#input()	Lê uma entrada do usuário.
#type()	Retorna o tipo de um objeto.
#len()	Retorna o tamanho (número de elementos) de um objeto iterável.
#id()	Retorna o identificador único de um objeto na memória.


#3. Funções
#Comando	O que faz
#def	Define uma função.
#return	Retorna um valor de uma função.
#lambda	Cria funções anônimas.
#python
#Copiar código
#def soma(a, b):
#    return a + b

#4. Manipulação de Listas, Tuplas, Dicionários e Conjuntos
#Listas
#Comando	O que faz
#list.append()	Adiciona um item ao final da lista.
#list.insert()	Adiciona um item em um índice específico.
#list.remove()	Remove um item específico.
#list.pop()	Remove e retorna o último item.
#list.sort()	Ordena a lista.
#list.reverse()	Inverte a ordem dos itens.
#python
#Copiar código
#lista = [3, 1, 2]
#lista.sort()  # [1, 2, 3]


#Dicionários
#Comando	O que faz
#dict.keys()	Retorna todas as chaves.
#dict.values()	Retorna todos os valores.
#dict.items()	Retorna pares (chave, valor).
#dict.get()	Obtém um valor sem erro caso a chave não exista.
#python
#Copiar código
#dados = {"nome": "Alice", "idade": 25}
#print(dados.get("nome"))  # Alice



#5. Entrada e Saída de Arquivos
#Comando	O que faz
#open()	Abre um arquivo.
#read()	Lê o conteúdo do arquivo.
#write()	Escreve no arquivo.
#close()	Fecha o arquivo.
#python
#Copiar código
#with open("arquivo.txt", "w") as f:
#    f.write("Hello, World!")