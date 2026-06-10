
#declaração de variáveis
user_selection = input("\n Digite 1 para acessar e 2 para encerrar: \n ")
retry = 0
diferenca = 0
logged_user = None

users = [
        {
        "type": "admin",
        "user_email": "admin@admin",
        "user_password": 1234,
        "saldo": 10000,
        "limite": 10000,
    },
        {
        "type": "user",
        "user_email": "chorenafeature@user",
        "user_password": 6767,
        "saldo": 6767,
        "limite": 86400,
    },
        {
        "type": "user",
        "user_email": "lucasguloso@user",
        "user_password": 6969,
        "saldo": 2440,
        "limite": 30,
    },
        {
        "type" : "user",
        "user_email": "aninhafazcompleto@user",
        "user_password": 8888,
        "saldo": 250,
        "limite": 3600,
    }
]


#função para mostrar opções do menu
def print_menu():
    print("\n- UNIVILLE Internet Banking -")

    if logged_user["type"] == "admin":
        print("0. Gerenciar Usuários")

    print("1. Consultar Saldo")
    print("2. Realizar Saque")
    print("3. Realizar Depósito")
    print("4. Consultar Limite")
    print("5. Encerrar")

#função para código inválido
def invalid_code():
    print("Valor inválido, tente novamente.")


if user_selection == '2':
    print("Encerrado")
    exit()
elif user_selection != '1':
    invalid_code()
    exit()
else:

# Loop para login 

    while retry < 3:

        user_email = input("Digite o seu e-mail: ")

        try:
            user_password = int(input("Digite a sua senha: "))
        except ValueError:
            invalid_code()
            continue

        logged_user = None

        for user in users:

            if (
                user["user_email"] == user_email
                and user["user_password"] == user_password
            ):
                logged_user = user
                break

        if logged_user:

            match logged_user["type"]:

                case "admin":
                    print("Bem vindo adm!", user_email)

                case "user":
                    print("Bem vindo usuário!", user_email)

                case _:
                    invalid_code()
                    exit()

            saldo = logged_user["saldo"]
            limite = logged_user["limite"]
            tipo = logged_user["type"]

            break

        retry += 1

        print(
            f"Tudo errado, tenta denovo parceiro, você tem mais {3 - retry} tentativas."
        )

    if retry >= 3:
        print("Deu a tua cota")
        exit()  
    # Loop do menu principal
    while True:
    
        try:   
            print_menu()
            user_selection_menu = input("Escolha uma opção: \n")
        except ValueError:
            invalid_code()
            continue

        #Gerenciar usuários
        if user_selection_menu == "0":
            if logged_user["type"] != "admin":
                invalid_code()

            else:
                for i, user in enumerate(users):
                    if user["type"] == "user":
                        print(f"{i}. {user['user_email']}")

                select = int(input("Escolhe um:"))

                select_user = users[select]
                print(f"Escolheu alguém meio parecido com {select_user['user_email']}")

                saldo = select_user['saldo']
                limite = select_user['limite']
                
            
                        
        if user_selection_menu == '1':
            while True:
                try:
                    print(f"Saldo: R${saldo:.2f}")
                    break
                except ValueError:
                        invalid_code()
                        continue
                

        # Saque
        elif user_selection_menu == '2':
            while True:
                try:
                    saque = float(input("Digite o valor do saque: "))
                    break
                except ValueError:
                    invalid_code()
                    continue
            if saldo + limite <= 0:
                    print(f"Saldo insuficiente para realizar o saque, falta R${ saque - abs(saldo + limite):.2f} para completar o saque.")
            else:
                    if saque > saldo:
                        diferenca = saque - saldo  
                        if diferenca > limite:
                            print(f"Saldo e limite insuficientes para realizar o saque, falta R${abs(saldo + limite - saque):.2f} para completar o saque.")
                            continue
                        limite -= diferenca  
                        saldo = 0
                    else:
                        select_user['saldo'] -= saque

                    print("Saque realizado com sucesso")
                    print(f"Saldo atual R$:", saldo)
                    

        # Depósito
        elif user_selection_menu == '3':
            while True:
                try:
                    deposito = float(input("Digite o valor do depósito: "))
                    break
                except ValueError:
                    invalid_code()
            if limite < 100:
                diferenca = 100 - limite  
                print(f"Limite total: {limite:.2f}")
                if deposito >= diferenca:
                    print(f"Depósito de R${deposito:.2f} completou o limite.")
                    limite = 100
                    saldo += deposito - diferenca 
                    print(f"Saldo atualizado: R${saldo:.2f}")
                else:
                    limite += deposito  
                    print(f"Limite atualizado: R${limite:.2f}")
            else:
                saldo += deposito
                print(f"Saldo atual: R${saldo:.2f}") 

                print("Depósito realizado com sucesso")

        # Consulta de limite
        elif user_selection_menu == '4':
            print(f"Limite: R${limite:.2f}") 

        # Encerrar
        elif user_selection_menu == '5':
            print("Encerrado")
            exit()
        else:
            invalid_code()