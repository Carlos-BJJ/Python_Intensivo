#Transferindo elementos de uma lista para outra

unconfirmed_users = ['mula', 'jagossauro', 'pentelhossauro']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

for confirmed_user in confirmed_users:
    print(f"{confirmed_user} Confirmed")

#Removendo TODAS os valores especificos de uma lista
#Com o loop while a função remove(), fica sendo executada até ser removido todos os valores desejados da lista

pets = ['dog', 'cat', 'fish', 'cat', 'rabbit', 'goldfish', 'cat']
print(f" \n{pets}")

while 'cat' in pets:
    pets.remove('cat')

print(f"\n{pets}")

#Preenchendo um dicionario com entrada do usuario

respostas = {}
ativado = True

while ativado:
    nome = input("\nQual é seu nome?")
    resposta = input("Fale um lugar onde vc gosta de ir: ")

    respostas[nome] = resposta

    repeticao = input("Quer continuar? (sim/nao)")
    if repeticao == "nao":
        ativado = False


for nome, resposta in respostas.items():
    print(f"O {nome} gosta de ir na(o) {resposta}")