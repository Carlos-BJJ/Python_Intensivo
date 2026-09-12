sandwich_orders = ['big mac','pastrami', 'mc lanch feliz','pastrami', 'big king','pastrami', 'sanduiche de presunto']

finished_sandwiches = []
print(f"\nSanduiches finalizados = {finished_sandwiches}")
print(f"\nSanduiches disponiveis = {sandwich_orders}\n")
print("O sanduiche de pastrami está indisponivel")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print("\nRemovendo pastrami...")
print(f"O sanduiche de pastrami foi removido do cardapio = {sandwich_orders}\n")

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()

    finished_sandwiches.append(current_sandwiches)

print("Preparando sanduiches...")
for sandwich in finished_sandwiches:
    print(f"\tO seu sanduiche {sandwich} está pronto")