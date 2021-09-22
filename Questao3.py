nome = input("Palavra: ")

if nome.endswith('o') or nome.endswith('O'):
    print(f'{nome}s')

else:
    print(f"\n{nome} não termina com letra 'o'")