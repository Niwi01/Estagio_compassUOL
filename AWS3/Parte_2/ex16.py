def soma(x):
    soma = 0
    for s in x:
      num = s.split(",") 
      for n in num:
        soma += int(n)
    print(soma)
    
soma(["1,3,4,6,10,76"])