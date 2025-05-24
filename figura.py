#print('-' *50)
#print('|',' '*46, '|')
#print('|',' '*46, '|')
#print('|',' '*46, '|')
#print('|',' '*46, '|')
#print('-' *50)

contador= 1
for i in range(20):
    print('#' * contador)
    contador+= 1

    print('\n')

    contador=1 
    espaco= 18
    for i in range(20):
        print(' '*espaco,contador * '#')
        contador= +2
        espaco= -1