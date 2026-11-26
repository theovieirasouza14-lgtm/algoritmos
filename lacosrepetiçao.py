print("-"*36)
print("| Exercicio de Laços de Repetição! |")
print("-"*36)

print("\nLaço For/Para\n")

for i in range(10):
    print(f"{i+1}ª volta!")
    
print("\nLaços de repetição condicionais\n")
print("- Laço While/Enquanto -")
op1=0
while op1==0:     #Este laço primeiro testa, depois faz
    print("Para saltar o do while digite 1 ou 0 para continuar")    
    op1=int(input("Digite 0 ou 1: "))
 
print("\n- Laço do While/Enquato -")
while True:     #Este laço primeiro FAZ, depois testa
         print("Para encerrar o exercicio digite 1 ou 0 para continuar")
         op2=int(input("Digite 0 ou 1: "))
         if op2==0:
             continue 
         else:
             print("\nExercico de laços encerrado pelo user!")
             break
         
         
         
         