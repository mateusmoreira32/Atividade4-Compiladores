string = input("Adicione um palavra ou uma frase: ")

contador= 0

for i in string:
    if i == 'a':
        contador = contador +1

if contador % 2 == 0:
    print(f"\nContagem de letras A em {string} é {str(contador)} que é PAR")


else:
    print(f"\nContagem de letras A em {string} é {str(contador)} que é IMPAR")
