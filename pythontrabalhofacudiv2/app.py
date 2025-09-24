print("numero: digite números maiores que 1, e use o -1 para cancelar") 
nums = [] 
while True: 
    try: 
        n = int(input()) 
    except: 
        print("isso esta errado") 
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
    d = 2 
    a, b = 1, n 
    while d <= n // 2: 
        if n % d == 0: 
            a, b = d, n // d 
            break 
        d += 1 
    print(f"{n}:{a}x{b}") 

if len(nums) > 0: 
    with open("atividade-gustavomelooliveira.txt", "w") as arq: 
        arq.write("n;d1;d2\n") 
        for n in nums: 
            d = 2 
            a, b = 1, n 
            while d <= n // 2: 
                if n % d == 0: 
                    a, b = d, n // d 
                    break 
                d += 1 
            arq.write(f"{n};{a};{b}\n") 
    print("relatorio foi gerado")