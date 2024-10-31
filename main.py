numero1= int(input('Digite o número 1:'))
numero2= int(input('Digite o número 2:'))
soma = 0
for numeropar in range(numero1, numero2):
    if numeropar % 2== 0:
        soma+= numero1
        print(f'{numeropar} par')
    
    else:
        print('Número impar')
   
print(f'A soma dos pares é {soma}')