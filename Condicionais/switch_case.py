opcao = int(input("Insira uma opção. 1 para \"Hello\", 2 para \"World\" e 3 para \"Hello World\"\n"))

match opcao:
    case 1:
        print("Hello")
    case 2:
        print("World")
    case 3:
        print("Hello World")