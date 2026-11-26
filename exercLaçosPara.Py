#01- Criar algoritmo que leia 3 nomes e imprima todos após a leitura 

print("-"*15)
print("| .: Nomes :. |")
print("-"*15)
nomes=[]

for i in range(3):
    nomes.append(input(f"Escreva seu {i+1}ª nome: "))
    
for nome in nomes:  # percorre cada elemento da lista
    print(nome)   #mostra cada nome na tela    