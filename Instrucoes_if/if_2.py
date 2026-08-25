#Verificando se uma lista não está vazia

ingredientes_pizza = []
#Se a lista tiver pelo menos 1 elemento ela é True, se for vazia ela será False

if ingredientes_pizza:
    for ingrediente in ingredientes_pizza:
        print(f"Adicionando o {ingrediente.title()}.")
    print("\nPizza finalizada!")

else:
    print("\nA lista de ingredientes está vazia, gostaria de uma pizza comum?\n")

#Exerciciozin

ordinais = list((range(1, 10)))
print(ordinais)

for ordinal in ordinais:
    if ordinal == 1:
        print("1st")
    elif ordinal == 2:
        print("2nd")
    elif ordinal == 3:
        print("3rd")
    else:
        print(f"{ordinal}th")