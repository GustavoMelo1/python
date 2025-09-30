# Trabalho de Algoritmos de Gustavo Melo Oliveira
# Feito no dia 24/09/2025 as 18:24 da tarde

print("digite números maior que 1, e use o -1 para cancelar")
vetor_gu = []
gustavo_div1 = []
gustavo_div2 = []

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
    if n in vetor_gu:
        print("tu já digitou esse numero, escreva outro")
        continue

    vetor_gu.append(n)

for n in vetor_gu:
    d = 2
    a, b = 1, n
    while d * d <= n:
        if n % d == 0:
            a, b = d, n // d
            break
        d += 1

    gustavo_div1.append(a)
    gustavo_div2.append(b)
    print(f"{n} divisores sao {a} e {b}")

if vetor_gu:
    with open("atividade-gustavomelooliveira.txt", "w", encoding="utf-8") as f:
        f.write("n;d1;d2\n")
        for i in range(len(vetor_gu)):
            f.write(f"{vetor_gu[i]};{gustavo_div1[i]};{gustavo_div2[i]}\n")
    print("relatório foi gerado")