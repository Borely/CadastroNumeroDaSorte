nome = input("Nome: ")
sobrenome = input("Sobrenome: ")
aniversario = input("Data de nascimento: ")
e_mail = input("E-mail: ")
codigo = input("Informe seu código e descubra se é nosso grande ganhador(a):")

while codigo != "15" and codigo != "23" and codigo != "145":
    tentar_novamente = input("Não foi dessa vez. Tentar novamente? " "Digite (s) para sim e (n) para não:")
    if tentar_novamente == "s":
         codigo = ""
         codigo = input("Informe o novo código:")
    else:
         print("Mais sorte da próxima vez!")
         break
if codigo == "15" or codigo == "23" or codigo == "145":
     print("Parabéns, você ganhou!")