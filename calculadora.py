def calcular(x,  y, op=1):
    if(op == 1):
      print("A soma é: ", x + y)
    elif(op == 2):  
      print("O resto é: ", x - y)
    elif(op == 3):  
      print("O produto é: ", x * y)
    elif(op == 4):  
      print("O quociente é: ", x / y)
    elif(op == 5):
      print("O resto da divisao é: ", x % y)
    elif(op == 6):
      print("A potencia é: ", x ** y)  

x = int(input("digite um numero "))
y = int(input("digite outro numero "))
print("OPERAÇÕES")
print("1 adiçao")
print("2 Subtraçao")
print("3 Multiplicaçao")
print("4 Divisão")
print("5 Resto da divisão")
print("6 Potencia")
op = int(input("Escolha a operação: "))
calcular(x, y, op)

