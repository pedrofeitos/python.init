maior = None
menor = None

for i in range(10):
    num = int(input(f"Digite o {i + 1 } numero positivo: "))

    if num <= 0:
        print("por favor, digite apenas numeros inteiros posotivos")
        continue

    if maior is None or num > maior:
        maior = num
    if menor is None or num < menor:
        menor = num

print(f"O maior numero é: {maior}")
print(f"O menor numero é: {menor}")
