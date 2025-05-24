print('sistema de calculo IMC')
#Criado por Junior
print('criado por junior')

#Dados do cliente
print('Dados do cliente')
nome=input('Digite seu nome:')
print(' ')
peso=float(input('Digite seu peso:'))
altura=float(input('Digite sua altura:'))
print(' ')

print('Calculo IMC')
IMC= peso/(altura*altura)
if (IMC< 19.1):
    print('Abaixo do peso')

elif(IMC > 19.1 and IMC <=25.8):
    print('peso normal')

elif(IMC > 25.8 and IMC <= 27.3):
    print('Acima do peso')

elif(IMC > 27.3 and IMC <= 32.3):
    print('Obesidade I')
elif(IMC > 32.3):
    print('Obesidade II')
