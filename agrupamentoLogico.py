#Agrupamento lógico
# Criar um algoritmo que recebe 4 notas em um vetor, receba a freq. do aluno, nome do aluno. Realize a média e avalie para ser aprovado a média >=7 e freq >=, 
# avaliar se reprovou por falta ou por nota e ao final apresentar o resultado.

print("Sistema de notas:. ")   #Titulo do console
notas=[]   #Atribui vetor a varial Notas
nome=input("Digite o nome do aluno: ")
for i in range(4):   # i= variavel contadora, range é o tamanho do vetor. (4 posiçoes: 0-3), for é quando se cria um laço de repetição. , i (incrementar in 4 posiçoes)
    nota=float(input(f"Digite a {i+1}ª nota: "))
    notas.append(nota) #append é pra adicionar/percorrer
    
freq=float(input("Digite a frequencia do aluno: "))
media=sum(notas)/len(notas)  
#sum= soma das notas, len pega o tamanho do vetor

if media>=7 and freq>=75:
    resultado="aprovado!"
elif freq<75:
    resultado="reprovado por falta."
else:
    resultado="reprovado por falta"
    
print("\n--- Resultado final ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Frequencia: {freq:.1f}%")
print(f"Resultado final: {resultado}")                  
    