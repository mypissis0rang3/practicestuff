def categorize_places():
    while True:
        places = input("\nInsira o título completo ou número (1 a 139) do artigo. Digite Menu para retornar:").lower()

        if places == "menu":
            print("Retornando ao menu")
            break

        incl = ["1" or "title 1", "2" or "title 2"]
        ninotavailable = ["3" or "title 3"]
        niwp = ["4" or "title 4"]
        nias = ["5" or "title 5"]
        niwt = ["6" or "title 6"]

        if places in ninotavailable:
            print("Não incluso. Motivo: Indisponível na íntegra-aberto online.")
        elif places in niwp:
            print("Não incluso. Motivo: População incompatível")
        elif places in nias:
            print("Não incluso. Motivo: Estudo com modelo animal")
        elif places in niwt:
            print("Não incluso. Motivo: Temática incompatível...incluir analise de instrumentos")
        
        elif places in incl:
            print("Incluso.")
            
        else:
            print("Inválido")

def list_results():
    while True:
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")

         x = input("Digite menu para retornar:").lower()
         if x == "menu":
             print("Retornando ao menu")
             break
         
def list_incl():
    while True:
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")
         print("1-   ")

         x = input("Digite menu para retornar:").lower()
         if x == "menu":
             print("Retornando ao menu")
             break

def list_ni():
    while True:
         print("Motivo: Indisponível na íntegra-aberto online")
         print("1-   ")
         print("Motivo: Estudo de modelo animal")
         print("1-   ")
         print("Motivo: População incompatível")
         print("1-   ")
         print("Motivo:Temática incompatível")
         print("1-   ")

         x = input("Digite menu para retornar:").lower()
         if x == "menu":
             print("Retornando ao menu")
             break


while True:
    print("\n[MENU]")
    print("1 - Busca de status da publicação")
    print("2 - Lista dos resultados de busca - sem duplicatas")
    print("3 - Lista de publicações inclusas")
    print("4 - Lista de publicações não inclusas e motivo")
    print("5 - Sair")

    x = input("Insira 1,2,3,4 ou 5:")

    if x == "1":
        categorize_places()
    if x == "2":
        list_results()
    if x == "3":
        list_incl()
    if x == "4":
        list_ni()
        

    elif x == "5":
        print("Saindo")
        break

    else:
        print("Inválido")