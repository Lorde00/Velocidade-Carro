multaporkm = 20.00

velocidademax = 80.00

velocidade = float(input('Qual a velocidade do veículo?\n'))

if velocidade > velocidademax:
    velocidadeult = velocidade - velocidademax
    multatotal = multaporkm * velocidadeult

    print(f'Você foi multado em R${multatotal}!\n')

else:
    print(f'Você não foi multado!\n')
    
