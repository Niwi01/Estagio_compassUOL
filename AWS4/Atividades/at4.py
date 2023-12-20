def calcular_valor_maximo(operadores, operandos):
    mudar = list(map(lambda x: eval(f'{x[1][0]}{x[0]}{x[1][1]}'), zip(operadores,operandos)))
    return max(mudar)
    
operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]
res = calcular_valor_maximo(operadores,operandos)
print(res)