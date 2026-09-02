#Aninhamento
#1. Lista de dicionarios
 
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'purple', 'points': 20}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

#criando 30 aliens verdes

aliens2 = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5}
    aliens2.append(new_alien)

print(f"Foram criados {len(aliens2)} aliens")

#Mudando a cor de 3 aliens

for alien2 in aliens2[:3]:
    if alien2['color'] == 'green':
        alien2['color'] = 'yellow'
        alien2['points'] = 10
    elif alien2['color'] == 'yellow':
        alien2['color'] = 'purple'
        alien2['points'] = 20

for alien2 in aliens2[:5]:
    print(alien2)


