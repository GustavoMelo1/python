"""
Trabalho de Algoritmos — Gustavo Melo Oliveira

Esse script faz a mesma coisa do app.py: lê números, acha divisores e salva num CSV.
A diferença é que aqui eu vou até n//2 pra procurar divisor.
Funciona, mas é bem mais lento pra números grandes.
É útil mais pra quem tá começando, porque fica mais fácil de entender a lógica.
"""

print("Digite números maiores que 1. Para encerrar, digite -1.")

# Lista que guarda os números válidos
numeros = []
# Lista de tuplas (n, a, b) com os divisores
pares = []

while True:
    try:
        n = int(input("Número: "))  # tento converter pra inteiro
    except ValueError:
        print("Entrada inválida, digita só número inteiro.")
        continue

    if n == -1:       # saída
        break
    if n <= 1:        # não aceito menor ou igual a 1
        print("O número precisa ser maior que 1.")
        continue
    if n in numeros:  # não aceito repetição
        print("Esse número já foi digitado, coloca outro.")
        continue

    numeros.append(n)

# agora procuro divisores até n//2
for n in numeros:
    a, b = 1, n   # padrão se for primo
    d = 2         # começo do teste

    while d <= n // 2:
        if n % d == 0:
            a, b = d, n // d
            break
        d += 1

    pares.append((n, a, b))
    print(f"{n} → {a} x {b}")  # mostro na tela

# gero o relatório
if pares:
    with open("atividade-gustavomelooliveira.txt", "w", encoding="utf-8", newline="") as f:
        f.write("n;d1;d2\n")
        for n, a, b in pares:
            f.write(f"{n};{a};{b}\n")

    print("Relatório salvo em 'atividade-gustavomelooliveira.txt'.")

# Nota pra quem tá chegando:
# 1 Essa versão aqui é mais lenta, mas é boa pra explicar a lógica sem pressa
# 2 Estrutura diferente do app.py: aqui eu guardo tuplas (n, a, b), lá uso listas paralelas
# 3 Pra produção, use o app.py, esse aqui é mais "didático"
