#Exericio04
#Faça um Programa que peça um número e então mostre a mensagem "O número informado foi: [número]
"""
while True:
  numero = int(input("Digite um numero: "))
  print("O numero digitado foi:",numero, "\n")
"""

#Exercicio05
"""
while True:
    word1 = input("Digita uma palavra com é:\n")
    print(word1.replace("é","e"))
    if word1 == "sair":
     break
"""

#Exercicio06
"""
while True:
 nome = input("Digite o seu nome: ")

 #salva a alteração feita através da manipulação da string
 nome = nome.upper() 

 pergunta = input("Quer comprar donuts? ")

#salva a alteração feita através da manipulação da string
 pergunta = pergunta.lower()
 pergunta = pergunta.replace("ã", "a")
 if pergunta == "sim" or pergunta == "quero":
     print(nome,"quer comprar donuts!")
 elif pergunta == "nao" or pergunta == "nao quero":
     print(nome,"vai perder a chance de se apaixonar pelos donuts.")
 else:
     print(nome,"tá só me enrolando, hein")

 print()
"""

#Exercicio07
arquivo = open("PesquisaDonuts.txt","w+")
nome = input("Digite o seu nome: ")
nome = nome.upper() 
pergunta = input("Quer comprar donuts? ")
#pergunta = pergunta.lower()
#pergunta = pergunta.replace("ã", "a")
if pergunta == "sim" or pergunta == "quero":
 arquivo.writelines(nome,"quer comprar donuts!")
elif pergunta == "nao" or "nao quero":
 arquivo.writelines(nome,"vai perder a chance de se apaixonar pelos donuts.")
else:
 arquivo.writelines(nome,"tá só me enrolando, hein")
