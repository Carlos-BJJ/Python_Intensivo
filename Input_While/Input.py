#Como input() funciona
    #A função espera a entrada do usuario e atribui a resposta a uma variavel

name = input("Digite seu nome: ")
print( f"Seu nome é {name}")

#Usando int para receber entradas numericas
    #A BIF input atribui toda entrada como se fosse string, então devemos usar a BIF int para converte o tipo de dado

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print(f"{num1} + {num2} é igual a {num1 + num2}")

