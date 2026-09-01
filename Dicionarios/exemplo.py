favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward' : 'rust',
    'phil' : 'python'
}

pesquisa = ['jen', 'sarah', 'edward', 'phil', 'carlos', 'joão']

for name in pesquisa:
    if name in favorite_language:
        print(f"Obrigado pela resposta da pesquisa, {name.title()}")
    else:
        print(f"Você está convidado a responder a pesquisa, {name.title()}")