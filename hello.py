print("=== Cálculo da Média Anual ===")

continuar= 'sim'
while continuar.lower().strip()== 'sim':
     
    nota1 = float(input("Digite a nota do 1º bimestre: "))
    while nota1 > 10:
        nota1 = float(input("ERRO.Digite a nota do 1º bimestre: "))
    nota2 = float(input("Digite a nota do 2º bimestre: "))
    while nota2 > 10:
         nota2 = float(input("ERRO.Digite a nota do 2º bimestre: "))
    nota3 = float(input("Digite a nota do 3º bimestre: "))
    while nota3 > 10:
         nota3 = float(input("ERRO.Digite a nota do 3º bimestre: "))
    nota4 = float(input("Digite a nota do 4º bimestre: "))
    while nota4 > 10:
         nota4 = float(input("ERRO.Digite a nota do 4º bimestre: "))
    media = (nota1 + nota2 + nota3 + nota4) / 4

    if  (media >=5):
        print('aluno Aprovado') 
        print('Parabens')

    elif (media>= 3):
            print('aluno de exame')
            
    else:        
        print('aluno Reprovado')
        print('Tente outra vez')

    continuar = input('continuar?<sim/Não> :')
    print('FIM DO PROGRAMA')
    

  