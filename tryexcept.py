#try again

try:
   a = int(input("digite o dividendo: "))
   c = int(input("digite o divisor: "))
   resultado = a / c
except ValueError:
  print("impossivel diividir por 0")
except ZeroDivisionError:
  print("voçê não digitou um numero válido")
else:
  print("nenhum erro.")
finally:
  print("este bloco sempre sera executado.")    



