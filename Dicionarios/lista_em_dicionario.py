#Uma lista em um dicionario 

pizza = {
     "borda": "fezes",
     "recheio": ["caroço", "estrogobofe", "feijão"]
}

#Aninhar loop for
favorite_language = {
    'jen': ['python', 'c'],
    'sarah': ['c', 'java'],
    'edward' : ['rust', 'go'],
    'phil' : ['python', 'c#']
}

for name, languages in favorite_language.items():
    print(f"\nA linguagem favorita de {name}:")
    for language in languages:
        print(f"\t{language.title()}")