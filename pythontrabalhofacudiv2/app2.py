# Trabalho de Algoritmos de Gustavo Melo Oliveira
# Feito no dia 24/09/2025 as 18:24 da tarde

print("digite números maior que 1, e use o -1 para cancelar")

nums = []
while True:
    try:
        n = int(input("número: "))
    except:
        print("so pode numeros")
        continue

    if n == -1:
        break
    if n <= 1:
        print("tem que ser maior que 1")
        continue
    if n in nums:
        print("tu já digitou esse, escreva outro")
        continue

    nums.append(n)

pares = []
for n in nums:
    d = 2
    a, b = 1, n
    while d <= n // 2:
        if n % d == 0:
            a, b = d, n // d
            break
        d += 1
    pares.append((n, a, b))
    print(f"{n}:{a}x{b}")

if pares:
    with open("atividade-gustavomelooliveira.txt", "w") as arq:
        arq.write("n;d1;d2\n")
        for n, a, b in pares:
            arq.write(f"{n};{a};{b}\n")
    print("relatorio foi gerado")