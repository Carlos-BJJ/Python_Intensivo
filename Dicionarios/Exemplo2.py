cities = {
        'RioDeJaneiro' : ['Brasil', '10M', 'Cidade Turistica'],
        'Sao paulo' : ['Brasil', '20M', 'Cidade poluida'],
        'Salvador' : ['Brasil', '5M', 'Praias lindas']
}

for city, facts in cities.items(): 
    print(f"\nA cidade é: {city}")
    print(f"E as informações dela são:")
    for infos in facts:
        print(f"\t{infos}")