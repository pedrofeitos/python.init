contador = 0


for i in range(5):
   numero = int(input(f"Digite o {i + 1}º número inteiro: "))


   if numero % 3 == 0:
       contador += 1


print(f"Quantidade de números divisíveis por 3: {contador}")
