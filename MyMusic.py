#Funções
def login():
    email = str(input("\033[35mDigite seu email: \n\033[m"))
    senha = str(input("\033[35mDigite sua senha: \n\033[m"))

    for i in range(len(cadastrados)):
        if(cadastrados[i][0] == email and cadastrados[i][2] == senha):
            
            #Página Vendedor

            if(cadastrados[i][3] == "V"):
                print("\033[32m\n Página dos vendedores\033[m")
                f = True
                while f:
                    try:
                        escomenu = int(input("\033[32m\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n\033[m"))
                        while(f):
                            
                            #Opção 1 no menu de vendedor
                            if(escomenu == 1):
                                a = "s"
                                while a == "s":
                                    nomeVend = str(input("\033[35mDigite o nome completo do novo vendedor: \033[m")).lower()
                                    for i in range(len(cadastrados)):
                                        if nomeVend == cadastrados[i][1]:
                                            cadastrados[i][3] = "V"
                                            print(cadastrados)
                                            a = input("\033[35mDeseja continuar? (s/n) \033[m")
                                            break
                                        if i == len(cadastrados)-1:
                                            print("Pessoa não encontrada")
                                            a = input("\033[35mDeseja continuar? (s/n) \033[m")
                                
                                escomenu = int(input("\033[32m\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n\033[m"))
                            
                            #Opção 2 no menu de vendedor
                            elif(escomenu == 2):
                                for i in range(len(cadastrados)):
                                    if(cadastrados[i][0] == email):
                                        new = int(input("\033[32m~ Digite o deseja modificar ~ \n1-Email\n2-Nome\n3-Senha\n4-Sair\033[m\n"))
                                        while(new < 4):
                                            if(new == 1):
                                                newemail = str(input("\033[35mDigite seu email: \n\033[m"))
                                                while not("@hotmail.com" in newemail or "@gmail.com" in newemail or "@outlook.com" in newemail): 
                                                    newemail = str(input("\033[31mEmail inválido\033[m \n\033[35mDigite seu email: \n\033[m"))
                                                cadastrados[i][0] = newemail  
                                            
                                            elif(new == 2):
                                                newname = str(input("\033[35mDigite seu nome: \n\033[m"))
                                                cadastrados[i][1] = newname
                                            
                                            elif(new == 3):
                                                newsenha = str(input("\033[35mDigite sua senha contendo letras e números: \n\033[m"))
                                                while (newsenha.isalpha() or newsenha.isdigit()):
                                                    newsenha = str(input("\033[31mSenha inválida \033[m \n\033[35mDigite sua senha contendo letras e números: \n\033[m"))
                                                cadastrados[i][2] = newsenha
                                            new = int(input("\033[32m~ Digite o deseja modificar ~ \n1-Email\n2-Nome\n3-Senha\n4-Sair\033[m\n"))
                                        print(cadastrados[i])
                                escomenu = int(input("\033[32m\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n\033[m"))

                            #Opção 3 no menu de vendedor
                            elif(escomenu == 3):
                                
                                #Menu da da Opção 2
                                print("\033[32m\n 1-Adicionar Produto \n 2-Produtos Esgotados \n 3-Reestocar Produtos \n 4-Deletar Produtos \n 5-Mostrar Estoque \n 6-Sair\033[m")
                                escoprod = int(input())

                                g = True
                                while(g):

                                    #Opção 1 dentro de produto
                                    if(escoprod == 1):
                                        nome = input("\033[35mDigite o Nome do Produto: \033[m").upper()
                                        while(nome == ""):
                                            print("\033[31mValor Inválido!\033[m")
                                            nome = input("\033[35mDigite o Nome do Produto: \033[m")
                                            
                                        valor = str(input("\033[35mDigite o Valor do Produto: \033[m"))
                                        while(valor.replace('.',',',1).isdigit() or valor == ""):
                                            print("\033[31mValor Inválido!\033[m")
                                            valor = str(input("\033[35mDigite o Valor do Produto: \033[m"))
                                        
                                        quant = str(input("\033[35mDigite a Quantidade em estoque do Produto: \033[m"))
                                        while(not(quant.isnumeric())):
                                            print("\033[31mValor Inválido!\033[m")
                                            quant = str(input("\033[35mDigite a Quantidade em estoque do Produto: \033[m"))
                                            
                                        descri = input("\033[35mDigite a Descrição do Produto: \033[m")
                                        while(descri == ""):
                                            print("\033[31mValor Inválido!\033[m")
                                            descri = input("\033[35mDigite a Descrição do Produto: \033[m")
                                            
                                        fab = input("\033[35mDigite a Fabricante do Produto: \033[m")
                                        while(fab == ""):
                                            print("\033[31mValor Inválido!\033[m")
                                            fab = input("\033[35mDigite a Fabricante do Produto: \033[m")
                                    
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
                                            name = input("\033[35mDigite o nome do produto que você quer como Esgotado: \033[m")
                                            if(name != "" and name.isalpha()):
                                                for i in range(len(instrumentos)):
                                                    if(name == instrumentos[i][0] and "Esgotado" not in instrumentos[i]):
                                                        instrumentos[i][2] = 0
                                                        Stresgo = "Esgotado"
                                                        instrumentos[i].append(Stresgo)
                                                        print(instrumentos[i])
                                                        b = False
                                                    elif("Esgotado" in instrumentos[i] and name == instrumentos[i][0]):
                                                        print("\033[36mProduto já Esgotado!\033[m")
                                                        b = False
                                            else: 
                                                print("\033[31mValor Inválido!\033[m")
                                                name = input("\033[35mDigite o nome do produto que você quer como Esgotado: \033[m")
                                    
                                    #Opção 3 dentro de produto   
                                    elif(escoprod == 3):
                                        c = True
                                        if(len(instrumentos) == 0):
                                            print("Não Há Produtos Registrados")
                                        while(c and len(instrumentos) != 0):
                                            name = input("\033[35mDigite o nome do produto que você quer como Reestocar: \033[m")
                                            while(name == ""):
                                                print("\033[31mOpção Inválida!! \n\033[m")
                                                name = input("\033[35mDigite o nome do produto que você quer como Reestocar: \033[m")
                                            d = False
                                            for i in range(len(instrumentos)):
                                                if(name == instrumentos[i][0] and "Esgotado" in instrumentos[i]):
                                                    reestoque = int(input("\033[35mDigite a nova quantidade do Produto: \033[m"))
                                                    instrumentos[i][2] = reestoque
                                                    instrumentos[i].pop()
                                                    print(instrumentos[i])
                                                    c = False
                                                    d = True
                                                else:
                                                    c = False
                                            if(not(d)):
                                                print("\033[31mOpção Inválida!! \n\033[m")
                                                    

                                    #Opção 4 dentro de produto      
                                    elif(escoprod == 4):
                                        e = False
                                        name = input("\033[35mDigite o nome do produto que você quer Deletar: \033[m")
                                        while(name == ""):
                                            print("\033[31mOpção Inválida!! \n\033[m")
                                            name = input("\033[35mDigite o nome do produto que você quer Deletar: \033[m")
                                        entrou = True
                                        for i in range(len(instrumentos)):
                                            if(entrou):
                                                if(name == instrumentos[i][0] and "Esgotado" in instrumentos[i]):
                                                    instrumentos.remove(instrumentos[i])
                                                    print(instrumentos)
                                                    e = True
                                                    entrou = False
                                        if(e == False):
                                            print("\033[31mOpção Inválida!! \n\033[m")

                                    
                                    #Opção 5 dentro de produto
                                    elif(escoprod == 5):
                                        print(instrumentos)
                                    
                                    #Opção 5 dentro de produto
                                    elif(escoprod == 6):
                                        g = False
                                        escomenu = 5

                                    #Opção inválida dentro de produto
                                    else:
                                        print("\033[31mOpção Inválida!! \n\033[m")
                                    
                                    #Retorno
                                    if(g):
                                        print("\033[32m\n 1-Adicionar Produto \n 2-Produtos Esgotados \n 3-Reestocar Produtos \n 4-Deletar Produtos \n 5-Mostrar Estoque \n 6-Sair\033[m")
                                        escoprod = int(input())

                            #Opção 4 no menu de vendedor                  
                            elif(escomenu == 4): 
                                f = False
                            
                            #Opção 5 no menu de vendedor
                            elif(escomenu == 5):
                                escomenu = escomenu = int(input("\033[32m\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n\033[m"))
                            
                            else: 
                                print("\033[31mOpção Inválida!! \n\033[m")
                                escomenu = int(input("\033[32m\n ~Menu de escolhas~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n\033[m"))
                            print("")
                    
                    except ValueError:
                        print("\033[31mOpção Inválida!! \n\033[m")       

            #Página Clientes
            elif(cadastrados[i][3] == "C"):
                print("\033[32m~Página dos Clientes\033[m")
                h = True
                while(h):
                    #Barra de Pesquisa
                    barra = input("\033[35mDigite o produto que deseja pesquisar: \033[m").upper()
                    j = True
                    for i in range(len(instrumentos)):
                        if(len(barra) > 2):
                            if(barra in instrumentos[i][0]):
                                print(instrumentos[i][0])
                                j = False
                            elif(len(instrumentos)-1 == i and j):
                                print("\033[31mProduto não encontrado! \033[m \n")

                            if(len(instrumentos)-1 == i and not(j)):
                                print("\033[32mDesejar saber mais sobre algum desses instrumentos? (s/n)\033[m")
                                opcao = str(input("")).lower()
                                if(opcao == "s"):
                                    pro = input("\033[35m\nDigite o nome do produto: \033[m").upper() 
                                    for i in range(len(instrumentos)):
                                        if(pro == instrumentos[i][0] and "Esgotado" not in instrumentos[i]):
                                            print(f"\033[36m\nNome: {instrumentos[i][0]} \nValor: {instrumentos[i][1]} \nQuantidade: {instrumentos[i][2]}\nDescrição: {instrumentos[i][3]} \nFabricante: {instrumentos[i][4]} \n\033[m")

                                            #Recomendação
                                            print("\n~ Recomendações ~")
                                            for i in range(len(instrumentos)):
                                                if(barra in instrumentos[i][0] and pro != instrumentos[i][0]):
                                                    print(instrumentos[i][0])
                                                    print("")

                                        elif(pro == instrumentos[i][0] and "Esgotado" in instrumentos[i]): 
                                            print(f"\033[36m\nNome: {instrumentos[i][0]} \nValor: {instrumentos[i][1]}\033[m \n\033[31mQuantidade: Esgotado \033[m\n\033[36mDescrição: {instrumentos[i][3]} \nFabricante: {instrumentos[i][4]} \n\033[m") 

                                            #Recomendação
                                            print("\033[32m\n~ Recomendações ~ \033[m")
                                            for i in range(len(instrumentos)):
                                                if(barra in instrumentos[i][0] and pro != instrumentos[i][0]):
                                                    print(instrumentos[i][0])
                                                    print("")
                                elif(opcao == "n"):
                                    pass
                                else:
                                    print("\033[31mOpção Inválida!!\n\033[m") 
                        
                        elif(len(instrumentos)-1 == i):
                            print("\033[31mOpção Inválida!!\033[m")
                        
            break
        
        if(i == len(cadastrados)-1):
             print("\033[31mInformações incorretas \n\033[m")
             escolhaLC = int(input("\033[32mCaso deseje fazer o Login digite (1). \nCaso deseje se Cadastrar digite (2). \n\033[m"))
             escolha = escolha(escolhaLC)
             logCad(escolha)
        
            
def logCad(escolhaLC):
    if(escolhaLC == 1):
        login()
            
    else:
        email = str(input("\033[35mDigite seu email: \n\033[m"))
        while not("@hotmail.com" in email or "@gmail.com" in email or "@outlook.com" in email): 
            email = str(input("\033[31mEmail inválido\033[m \n\033[35mDigite seu email: \n\033[m"))            

        nome = str(input("\033[35mDigite seu nome: \n\033[m"))

        senha = str(input("\033[35mDigite sua senha contendo letras e números: \n\033[m"))
        while (senha.isalpha() or senha.isdigit()):
            senha = str(input("\033[31mSenha inválida \033[m \n\033[35mDigite sua senha contendo letras e números: \n\033[m"))
        categoria = "C"

        usuario = [email, nome, senha, categoria]
        cadastrados.append(usuario)
        print(cadastrados)

        print("Cadastro Concluido!")
        print(" ")
        login()
            
               
#MAIN
instrumentos = [["GUITARRAWOODSTOCK", 1017.9, 7, "Guitarra Woodstock Series TG-530 Preta", "Tagima", "Esgotado"], ["PIANODIGITAL", 5241.5, 1, "Piano Digital Modelo P125B Preto", "Yamaha"], ["GUITARRATELECASTA", 2400.6, 3, "Guitarra Telecasta Series TC-530 Branco", "Yamaha"]]
cadastrados = [["adm@gmail.com", "adm", "adm123", "V"], ["patty@gmail.com", "patty", "321patty", "C"], ["robert@hotmail.com", "robert", "a123", "V"]]

while True:
        try:
            escolhaLC = int(input("\033[32mCaso deseje fazer o Login digite (1). \nCaso deseje se Cadastrar digite (2). \n\033[m"))
            if(escolhaLC == 1 or escolhaLC == 2):
                logCad(escolhaLC)
        except ValueError:
            print("\033[31mOpção Inválido!\033[m")

