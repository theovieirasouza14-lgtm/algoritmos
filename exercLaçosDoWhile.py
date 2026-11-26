#Criar um algoritmo que leia uma senha, enquanto a senha for != "SenacTech", leia novamente a senha, quando acertar exibe mensagem que acertou a senha.

print("-"*15)
print("|.: senhas :. |")
print("-"*15)

while True:
    op=input("Digite uma senha: ")    #Não tem int pq ele converte valor em numero
    if op.lower()=="senactech":                 #  ->>>> é um metodo que transforma todas as letras de um texto em MINUSCULAS 
        print("\nParabens!Voce acertou a senha!!")
        break
    else:
        print("\nTente novamente!!")    
        continue