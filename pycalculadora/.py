while True:

    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    print("1 - soma")
    print("2 - divisao")
    print("3 - multiplicacao")
    print("4 - subtracao")
    
    op = input("Escolha o tipo de calculo: ").strip()

    if op == "1":
        print(num1 + num2)
    
    elif op == "2":
        if num2 != 0:
            print(num1 / num2) 
    
    elif op == "3":
        print(num1 * num2)

    elif op == "4":
        print(num1 - num2)

    else:
        print("Nao existe")
