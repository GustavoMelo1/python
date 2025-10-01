"""
Trabalho de Algoritmos — Gustavo Melo Oliveira

Esse script recebe números inteiros maiores que 1, até o usuário digitar -1.
Pra cada número, ele acha um par de divisores (a, b) tal que a * b = n.
Se o número for primo, fica 1 e o próprio número.
No final, gera um arquivo CSV com todos os resultados.

Aqui eu usei uma busca otimizada: só vou até a raiz quadrada do número.
Isso porque se um número tem divisor, eu encontro nesse intervalo.
Assim o programa fica bem mais rápido do que testar até n//2.
"""




print("Digite números maiores que 1. Para encerrar, digite -1.")

# Lista que vai guardar todos os números válidos que o usuário digitou
numeros = []
# Listas paralelas pra guardar o par de divisores de cada número
d1_lista = []
d2_lista = []

while True:
    try:
        n = int(input("Número: "))  # leio a entrada e tento converter pra inteiro
    except ValueError:
        print("Entrada inválida, digita só número inteiro.")
        continue

    if n == -1:        # -1 é o comando de saída
        break
    if n <= 1:         # não aceito número menor ou igual a 1
        print("O número precisa ser maior que 1.")
        continue
    if n in numeros:   # não aceito repetir número
        print("Esse número já foi digitado, coloca outro.")
        continue

    numeros.append(n)  # se passou nas regras, guardo o número

# agora, pra cada número, vou procurar divisores
for n in numeros:
    a, b = 1, n  # valor padrão (caso seja primo)
    d = 2        # começo a testar pelo 2

    # só preciso testar até a raiz quadrada
    while d * d <= n:
        if n % d == 0:     # achei um divisor
            a, b = d, n // d
            break          # não preciso continuar, já tenho um par
        d += 1

    d1_lista.append(a)
    d2_lista.append(b)

    # mostro o resultado na tela
    print(f"{n} → divisores: {a} e {b}")

# gero um relatório CSV simples com os resultados
if numeros:
    with open("atividade-gustavomelooliveira.txt", "w", encoding="utf-8", newline="") as f:
        f.write("n;d1;d2\n")  # cabeçalho estilo planilha
        for i in range(len(numeros)):
            f.write(f"{numeros[i]};{d1_lista[i]};{d2_lista[i]}\n")

    print("Relatório salvo em 'atividade-gustavomelooliveira.txt'.")

# Nota pra quem cair de paraquedas nesse código:
# 1 Se quiser deixar aceitar repetição de número, tira o if n in numeros
# 2 O formato CSV abre direto no Excel, mas dá pra trocar pra csv.writer se precisar algo mais robusto
# 3 Essa versão aqui é a indicada pra usar no dia a dia, porque é bem mais rápida