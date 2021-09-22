def split(numero):
    return [char for char in numero]

lsta1 = [11, 18, 19, 99, 99, 19,18,25,82,0,5,82,152,1222,]

num = input('Adicione um Palavra: ').upper()
lsta2 = split(num)

print(''.join([str(a) + b for a, b in zip(lsta1, lsta2)]))