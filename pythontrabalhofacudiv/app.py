def ler_numeros():
    vet_gu = []
    while True:
        try:
            n = int(input("Número: "))
        except ValueError:
            continue
        if n == -1:
            break
        if n > 1 and n not in vet_gu:
            vet_gu.append(n)
    return vet_gu

def primeira_dupla(n):
    d = 2
    while d < n:
        if n % d == 0:
            return d, n // d
        d += 1
    return 1, n

vet_gu = ler_numeros()
if vet_gu:
    gu_div1, gu_div2 = [], []
    for n in vet_gu:
        a, b = primeira_dupla(n)
        gu_div1.append(a)
        gu_div2.append(b)
        print(f"{n} tem divisores {a} e {b}")
    with open("relat_gu.csv", "w", encoding="utf-8") as f:
        for n, a, b in zip(vet_gu, gu_div1, gu_div2):
            f.write(f"{n},{a},{b}\n")
