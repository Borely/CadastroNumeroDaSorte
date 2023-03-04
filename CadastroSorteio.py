nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
aniversario = input("Data de nascimento: ")
e_mail = input("E-mail: ")
print("Deseja cadastrar?")
sim_ou_nao = input("sim ou não: ")
if sim_ou_nao == "sim":
        print("Vamos começar!")
        codigo = input("Digite o código: ")
        if codigo == "15":
             print("Parabéns, você ganhou!")
        else:
               print("Continue tentando!")
else:
       print("Ok! Até a próxima!")
       
        
    