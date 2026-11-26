#02- Criar algoritmo que leia um numero inteiro, enquanto este numero == impar leia novamente e só encerra quando o numero for Par

print("-"*30)
print("| .: ALGORITMO PAR/IMPAR :. |")
print("-"*30)

while True:     #While true cria um laço infinitamente ate voce mandar parar!
    op=int(input("\nDigite um numero par ou impar: "))
    if op % 2==0:
        print("Numero par, sistema encerrado pelo usuario!")
        break
    else:
        print("\nImpar, tente novamente sair do sistema.")