#Funções
def login():
    email = str(input("Digite seu email: \n"))
    senha = str(input("Digite sua senha: \n"))

    for i in range(len(cadastrados)):
        if(cadastrados[i][0] == email and cadastrados[i][2] == senha):
            
            #Página Vendedor

            if(cadastrados[i][3] == "V"):
                print("\n Pagina dos vendedores")
                f = True
                while f:
                    try:
                        escomenu = int(input("\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Alterações nos Produtos \n 3-Sair \n"))
                        while(f):
                            
                            #Opção 1 no menu de vendedor
                            if(escomenu == 1):
                                a = "s"
                                while a == "s":
                                    nomeVend = str(input("Digite o nome completo do novo vendedor: ")).lower()
                                    for i in range(len(cadastrados)):
                                        if nomeVend == cadastrados[i][1]:
                                            cadastrados[i][3] = "V"
                                            print(cadastrados)
                                            a = input("Deseja continuar? (s/n) ")
                                            break
                                        if i == len(cadastrados)-1:
                                            print("Pessoa não encontrada")
                                            a = input("Deseja continuar? (s/n) ")
                                
                                escomenu = int(input("\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Alterações nos Produtos \n 3-Sair \n"))
                            
                            #Opção 2 no menu de vendedor
                            elif(escomenu == 2):
                                
                                #Menu da da Opção 2
                                print("\n 1-Adicionar Produto \n 2-Produtos Esgotados \n 3-Reestocar Produtos \n 4-Deletar Produtos \n 5-Mostrar Estoque \n 6-Sair")
                                escoprod = int(input())

                                g = True
                                while(g):

                                    #Opção 1 dentro de produto
                                    if(escoprod == 1):
                                        nome = input("Digite o Nome do Produto: ")
                                        while(nome == ""):
                                            print("Valor Inválido!")
                                            nome = input("Digite o Nome do Produto: ")
                                            
                                        valor = str(input("Digite o Valor do Produto: "))
                                        while(valor.replace('.',',',1).isdigit() or valor == ""):
                                            print("Valor Inválido!")
                                            valor = str(input("Digite o Valor do Produto: "))
                                        
                                        quant = str(input("Digite a Quantidade em estoque do Produto: "))
                                        while(not(quant.isnumeric())):
                                            print("Valor Inválido!")
                                            quant = str(input("Digite a Quantidade em estoque do Produto: "))
                                            
                                        descri = input("Digite a Descrição do Produto: ")
                                        while(descri == ""):
                                            print("Valor Inválido!")
                                            descri = input("Digite a Descrição do Produto: ")
                                            
                                        fab = input("Digite a Fabricante do Produto: ")
                                        while(fab == ""):
                                            print("Valor Inválido!")
                                            fab = input("Digite a Fabricante do Produto: ")
                                    
                                        #Adicição na lista os produtos
                                        valor = float(valor)
                                        quant = int(quant)
                                        produto = [nome, valor, quant, descri, fab]

                                        #Adiciona os produtos na lista de instrumentos 
                                        instrumentos.append(produto)
                                        print("")
                                        print(instrumentos)
                                    
                                    #Opção 2 dentro de produto
                                    elif(escoprod == 2):
                                        b = True
                                        if(len(instrumentos) == 0):
                                            print("Não Há Produtos Registrados!")
                                        while(b and len(instrumentos) != 0):
                                            name = input("Digite o nome do produto que você quer como Esgotado: ")
                                            if(name != "" and name.isalpha()):
                                                for i in range(len(instrumentos)):
                                                    if(name == instrumentos[i][0] and "Esgotado" not in instrumentos[i]):
                                                        instrumentos[i][2] = 0
                                                        Stresgo = "Esgotado"
                                                        instrumentos[i].append(Stresgo)
                                                        print(instrumentos[i])
                                                        b = False
                                                    elif("Esgotado" in instrumentos[i] and name == instrumentos[i][0]):
                                                        print("Produto já Esgotado!")
                                                        b = False
                                            else: 
                                                print("Valor Inválido")
                                                name = input("Digite o nome do produto que você quer como Esgotado: ")
                                    
                                    #Opção 3 dentro de produto   
                                    elif(escoprod == 3):
                                        c = True
                                        if(len(instrumentos) == 0):
                                            print("Não Há Produtos Registrados")
                                        while(c and len(instrumentos) != 0):
                                            name = input("Digite o nome do produto que você quer como Reestocar: ")
                                            while(name == ""):
                                                print("Opção Inválida!! \n")
                                                name = input("Digite o nome do produto que você quer como Reestocar: ")
                                            d = False
                                            for i in range(len(instrumentos)):
                                                if(name == instrumentos[i][0] and "Esgotado" in instrumentos[i]):
                                                    reestoque = int(input("Digite a nova quantidade do Produto: "))
                                                    instrumentos[i][2] = reestoque
                                                    instrumentos[i].pop()
                                                    print(instrumentos[i])
                                                    c = False
                                                    d = True
                                                else:
                                                    c = False
                                            if(not(d)):
                                                print("Opção Inválida!! \n")
                                                    

                                    #Opção 4 dentro de produto      
                                    elif(escoprod == 4):
                                        e = False
                                        name = input("Digite o nome do produto que você quer Deletar: ")
                                        while(name == ""):
                                            print("Opção Inválida!! \n")
                                            name = input("Digite o nome do produto que você quer Deletar: ")
                                        entrou = True
                                        for i in range(len(instrumentos)):
                                            if(entrou):
                                                if(name == instrumentos[i][0] and "Esgotado" in instrumentos[i]):
                                                    instrumentos.remove(instrumentos[i])
                                                    print(instrumentos)
                                                    e = True
                                                    entrou = False
                                        if(e == False):
                                            print("Opção Inválida!! \n")

                                    
                                    #Opção 5 dentro de produto
                                    elif(escoprod == 5):
                                        print(instrumentos)
                                    
                                    #Opção 5 dentro de produto
                                    elif(escoprod == 6):
                                        g = False
                                        escomenu = 4

                                    #Opção inválida dentro de produto
                                    else:
                                        print("Opção Inválida!! \n")
                                    
                                    #Retorno
                                    if(g):
                                        print("\n 1-Adicionar Produto \n 2-Produtos Esgotados \n 3-Reestocar Produtos \n 4-Deletar Produtos \n 5-Mostrar Estoque \n 6-Sair")
                                        escoprod = int(input())

                            #Opção 3 no menu de vendedor                  
                            elif(escomenu == 3): 
                                f = False
                            
                            #Opção 4 no menu de vendedor
                            elif(escomenu == 4):
                                escomenu = int(input("\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Alterações nos Produtos \n 3-Sair \n"))
                            
                            else: 
                                print("Opção Inválida!! \n")
                                escomenu = int(input("\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Alterações nos Produtos \n 3-Sair \n"))
                            print("")
                    except ValueError:
                        print("Opção Inválida!! \n")       

                #Página Clientes
                if(cadastrados[i][3] == "C"):
                    print("Página dos Clientes")
                break
        
        if(i == len(cadastrados)-1):
             print("Informações incorretas \n")
             escolhaLC = int(input("Caso deseje fazer o Login digite (1). \nCaso deseje se Cadastrar digite (2). \n"))
             escolha = escolha(escolhaLC)
             logCad(escolha)
        
            
def logCad(escolhaLC):
    if(escolhaLC == 1):
        login()
            
    else:
        email = str(input("Digite seu email: \n"))
        while not("@hotmail.com" in email or "@gmail.com" in email or "@outlook.com" in email): 
            email = str(input("Email inválido \nDigite seu email: \n"))            

        nome = str(input("Digite seu nome: \n"))

        senha = str(input("Digite sua senha contendo letras e números: \n"))
        while (senha.isalpha() or senha.isdigit()):
            senha = str(input("Senha inválida \nDigite sua senha contendo letras e números: \n"))
        categoria = "C"

        usuario = [email, nome, senha, categoria]
        cadastrados.append(usuario)
        print(cadastrados)

        print("Cadastro Concluido!")
        print(" ")
        login()
            
               
#MAIN
instrumentos = [["a", 56.9, 5, "gfdsd", "gdsjf"], ["b", 809.9, 5, "gfddfdsd", "gdsfdfjf"]]
cadastrados = [["adm@gmail.com", "adm", "adm@gmail.com", "V"], ["patty@gmail.com", "patty", "patty@gmail.com", "C"]]

while True:
        try:
            escolhaLC = int(input("Caso deseje fazer o Login digite (1). \nCaso deseje se Cadastrar digite (2). \n"))
            if(escolhaLC == 1 or escolhaLC == 2):
                logCad(escolhaLC)
        except ValueError:
            
            print("Opção Invalida")

