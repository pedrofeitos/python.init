def maiorNumero (num1, num2, num3):
    if (num1 >= num2 >= num3):
        print("O" , num1, "é maior")
        if (num2 >= num1 >= num3):
          print("O", num2, "é maior")
           if (num3 >= num1 >= num2):
             print("O", num3, "é maior")


num1 = int(input("digite um numero: "))
num2 = int(input("digite um segundo numero:"))
num3 = int(input("digite um terceiro numero; "))
maiorNumero(num1, num2, num3)