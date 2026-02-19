
cpf = input('Digite o seu cpf: ')\
    .replace('.','')\
    .replace('-','')\
    .replace(' ','')\
    
entrada_sequencial = cpf == cpf[0] * len(cpf) 

##########################
#PRIMEIRO DIGITO VERIFICADOR
##########################

numeros = []
for digito in cpf[:9]:
    numeros.append(digito)

regressivo = 10
mult = []

#Contagem regressiva de 10 a 2
while regressivo > 2:
    #multiplicação do digito do cpf com o numero da regressiva
    for i in numeros:
       mult.append(int(i) * regressivo)
       regressivo += -1
    
#soma as multiplicações
soma = 0
for i in mult:
    soma += i

#Pega o resto da divisao do numero
x = soma * 10
resto = x % 11

#verifica o 1 digito do cpf
if resto <= 9:
    primeiro_digito = resto
else:
    primeiro_digito = '0'

##########################
#SEGUNDO DIGITO VERIFICADOR
##########################

#adciona o primeiro digito aos outros 9 anteriores
numeros.append(primeiro_digito)

regressivo = 11
mult = []

#Contagem regressiva de 11 a 2
while regressivo > 2:
    #multiplicação do digito do cpf com o numero da regressiva
    for i in numeros:
       mult.append(int(i) * regressivo)
       regressivo += -1

soma = 0
for i in mult:
    soma += i

#Pega o resto da divisao do numero
soma_10 = soma * 10
resto = soma_10 % 11

#verifica o 2 digito do cpf
if resto <= 9:
    segundo_digito = resto
else:
    segundo_digito = '0'

#verificação do CPF
if entrada_sequencial:
    print('CPF Inválido')
elif cpf[9] == str(primeiro_digito) and cpf[10] == str(segundo_digito):
    print('CPF Válido')
else:
    print('CPF Inválido')





    




    

