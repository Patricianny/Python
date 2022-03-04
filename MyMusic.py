#Funções
from sys import call_tracing


def login():
    t = True
    email = str(input("\033[35m Digite seu email: \033[m"))
    senha = str(input("\033[35m Digite sua senha: \033[m"))
    newemail = ""
    for i in range(len(cadastrados)):
        f = True
        z = True
        r = True
        carrinho = []
        if(cadastrados[i][0] == email and cadastrados[i][2] == senha):
            
            #Página Vendedor

            if(cadastrados[i][3] == "V"):
                print("\033[32m\n~ Página dos vendedores ~\033[m")
                while f:
                    try:
                        escomenu = int(input("\033[32m\n ~ Menu de escolhas ~ \n 1-Adicionar  vendedores \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n ➱ \033[m"))
                        while(f):
                            
                            #Opção 1 no menu de vendedor
                            if(escomenu == 1):
                                a = "s"
                                while a == "s":
                                    nomeVend = str(input("\n\033[35m Digite o nome completo do novo vendedor: \033[m")).lower()
                                    for i in range(len(cadastrados)):
                                        if nomeVend == cadastrados[i][1]:
                                            cadastrados[i][3] = "V"
                                            print(cadastrados)
                                            a = input("\n\033[35m Deseja continuar? (s/n) \033[m")
                                            break
                                        if i == len(cadastrados)-1:
                                            print(" Pessoa não encontrada")
                                            a = input("\n\033[35m Deseja continuar? (s/n) \033[m")
                                
                                escomenu = int(input("\033[32m\n ~ Menu de escolhas ~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n ➱ \033[m"))
                            
                            #Opção 2 no menu de vendedor
                            elif(escomenu == 2):
                                for i in range(len(cadastrados)):
                                    if(cadastrados[i][0] == email):
                                        new = int(input("\n\033[32m ~ Digite o deseja modificar ~ \n 1-Email \n 2-Nome \n 3-Senha \n 4-Deletar Cadastro \n 5-Sair \n ➱ \033[m"))
                                        while(new < 5):
                                            if(new == 1):
                                                newemail = str(input("\n\033[35m Digite seu email: \033[m")).lower()

                                                while not("@hotmail.com" in newemail or "@gmail.com" in newemail or "@outlook.com" in newemail) or newemail == email: 
                                                    newemail = str(input("\033[31m Email inválido!!\n\033[m \n\033[35m Digite seu email: \033[m")).lower()
                                                
                                                cadastrados[i][0] = newemail  
                                            
                                            elif(new == 2):
                                                for i in range(len(cadastrados)):
                                                    if(email == cadastrados[i][0] or newemail == cadastrados[i][0]):
                                                        name = cadastrados[i][1].lower()
                                                        newname = str(input("\n\033[35m Digite seu nome: \033[m")).lower()
                                                        while(newname == "" or newname == name or newname.isnumeric()):
                                                            print("\033[31m Opção Inválida!! \n\033[m")
                                                            newname = str(input("\033[35m Digite seu nome: \033[m")).lower()
                                                        cadastrados[i][1] = newname

                                            elif(new == 3):
                                                newsenha = str(input("\n\033[35m Digite sua senha contendo letras e números: \033[m"))
                                                while(newsenha.isalpha() or newsenha.isdigit() or newsenha == "" or newsenha == senha):
                                                    newsenha = str(input("\033[31m Senha inválida!!\n\033[m \n\033[35m Digite sua senha contendo letras e números: \033[m"))
                                                cadastrados[i][2] = newsenha

                                            elif(new == 4):
                                                excluir = input("\n\033[35m Tem certeza que deseja apagar sua conta? (s/n) \033[m").lower()
                                                while(excluir != "s" and excluir != "n"):
                                                    print("\033[31m Valor Inválido!!\033[m") #cor
                                                    excluir = input("\n\033[35m Tem certeza que deseja apagar sua conta? (s/n) \033[m").lower()
                                                if(excluir == "s"):
                                                    for i in range(len(cadastrados)):
                                                        if(email == cadastrados[i][0] or newemail == cadastrados[i][0]):
                                                            cadastrados.remove(cadastrados[i])
                                                            print("\033[31m Removido\033[m \n")
                                                            print(cadastrados, "\n")
                                                            login()

                                            print(cadastrados[i])
                                            
                                            new = int(input("\n\033[32m ~ Digite o deseja modificar ~ \n 1-Email \n 2-Nome \n 3-Senha \n 4-Deletar Cadastro \n 5-Sair \n ➱ \033[m"))


                                escomenu = int(input("\033[32m\n ~ Menu de escolhas ~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n ➱ \033[m"))

                            #Opção 3 no menu de vendedor
                            elif(escomenu == 3):
                                
                                #Menu da da Opção 2
                                print("\033[32m\n 1-Adicionar Produto \n 2-Produtos Esgotados \n 3-Reestocar Produtos \n 4-Deletar Produtos \n 5-Mostrar Estoque \n 6-Sair\033[m")
                                escoprod = int(input("\033[32m ➱ \033[m"))

                                g = True
                                while(g):

                                    #Opção 1 dentro de produto
                                    if(escoprod == 1):
                                        nome = input("\n\033[35m Digite o Nome do Produto: \033[m").upper()
                                        while(nome == ""):
                                            print("\033[31m Valor Inválido!!\033[m")
                                            nome = input("\n\033[35m Digite o Nome do Produto: \033[m")
                                            
                                        valor = str(input("\n\033[35m Digite o Valor do Produto: \033[m"))
                                        while(valor.replace('.',',',1).isdigit() or valor == ""):
                                            print("\033[31m Valor Inválido!!\033[m")
                                            valor = str(input("\n\033[35m Digite o Valor do Produto: \033[m"))
                                        
                                        quant = str(input("\n\033[35m Digite a Quantidade em estoque do Produto: \033[m"))
                                        while(not(quant.isnumeric())):
                                            print("\033[31m Valor Inválido!!\033[m")
                                            quant = str(input("\n\033[35m Digite a Quantidade em estoque do Produto: \033[m"))
                                            
                                        descri = input("\n\033[35m Digite a Descrição do Produto: \033[m")
                                        while(descri == ""):
                                            print("\033[31m Valor Inválido!!\033[m")
                                            descri = input("\n\033[35m Digite a Descrição do Produto: \033[m")
                                            
                                        fab = input("\n\033[35m Digite a Fabricante do Produto: \033[m")
                                        while(fab == ""):
                                            print("\033[31m Valor Inválido!!\033[m")
                                            fab = input("\n\033[35m Digite a Fabricante do Produto: \033[m")
                                    
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
                                            print("\033[34m\033[m\n Não Há Produtos Registrados!\033[m")
                                        while(b and len(instrumentos) != 0):
                                            name = input("\n\033[35m Digite o nome do produto que você quer como Esgotado: \033[m")
                                            if(name != "" and name.isalpha()):
                                                for i in range(len(instrumentos)):
                                                    if(name == instrumentos[i][0] and "Esgotado" not in instrumentos[i]):
                                                        instrumentos[i][2] = 0
                                                        Stresgo = "Esgotado"
                                                        instrumentos[i].append(Stresgo)
                                                        print(instrumentos[i])
                                                        b = False
                                                    elif("Esgotado" in instrumentos[i] and name == instrumentos[i][0]):
                                                        print("\n\033[36m Produto já Esgotado!!\033[m")
                                                        b = False
                                            else: 
                                                print("\n\033[31m Valor Inválido!!\033[m")
                                                name = input("\n\033[35m Digite o nome do produto que você quer como Esgotado: \033[m")
                                    
                                    #Opção 3 dentro de produto   
                                    elif(escoprod == 3):
                                        c = True
                                        if(len(instrumentos) == 0):
                                            print("\n Não Há Produtos Registrados!")
                                        while(c and len(instrumentos) != 0):
                                            name = input("\n\033[35m Digite o nome do produto que você quer como Reestocar: \033[m")
                                            while(name == ""):
                                                print("\n\033[31m Opção Inválida!! \n\033[m")
                                                name = input("\n\033[35m Digite o nome do produto que você quer como Reestocar: \033[m")
                                            d = False
                                            for i in range(len(instrumentos)):
                                                if(name == instrumentos[i][0] and "Esgotado" in instrumentos[i]):
                                                    reestoque = int(input("\n\033[35m Digite a nova quantidade do Produto: \033[m"))
                                                    instrumentos[i][2] = reestoque
                                                    instrumentos[i].pop()
                                                    print(instrumentos[i])
                                                    c = False
                                                    d = True
                                                else:
                                                    c = False
                                            if(not(d)):
                                                print("\n\033[31m Opção Inválida!!\n\033[m")
                                                    

                                    #Opção 4 dentro de produto      
                                    elif(escoprod == 4):
                                        e = False
                                        name = input("\n\033[35m Digite o nome do produto que você quer Deletar: \033[m")
                                        while(name == ""):
                                            print("\n\033[31m Opção Inválida!! \n\033[m")
                                            name = input("\n\033[35m Digite o nome do produto que você quer Deletar: \033[m")
                                        entrou = True
                                        for i in range(len(instrumentos)):
                                            if(entrou):
                                                if(name == instrumentos[i][0] and "Esgotado" in instrumentos[i]):
                                                    instrumentos.remove(instrumentos[i])
                                                    print(instrumentos)
                                                    e = True
                                                    entrou = False
                                        if(e == False):
                                            print("\n\033[31m Opção Inválida!!\033[m")

                                    
                                    #Opção 5 dentro de produto
                                    elif(escoprod == 5):
                                        print(instrumentos)
                                    
                                    #Opção 5 dentro de produto
                                    elif(escoprod == 6):
                                        g = False
                                        escomenu = 5

                                    #Opção inválida dentro de produto
                                    else:
                                        print("\n\033[31m Opção Inválida!!\033[m")
                                    
                                    #Retorno
                                    if(g):
                                        print("\n\033[32m\n 1-Adicionar Produto \n 2-Produtos Esgotados \n 3-Reestocar Produtos \n 4-Deletar Produtos \n 5-Mostrar Estoque \n 6-Sair\033[m")
                                        escoprod = int(input("\033[32m ➱ \033[m"))

                            #Opção 4 no menu de vendedor                  
                            elif(escomenu == 4): 
                                f = False
                            
                            #Opção 5 no menu de vendedor
                            elif(escomenu == 5):
                                escomenu = escomenu = int(input("\n\033[32m\n ~ Menu de escolhas ~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n ➱ \033[m"))
                            
                            else: 
                                print("\n\033[31m Opção Inválida!!\033[m")
                                escomenu = int(input("\n\033[32m\n ~ Menu de escolhas ~ \n 1-Adicionar  vendedores. \n 2-Atualizar Cadastro \n 3-Alterações nos Produtos \n 4-Sair \n ➱ \033[m"))
                            print("")
                    
                    except ValueError:
                        print("\n\033[31m Opção Inválida!!\033[m")       

            #Página Clientes
            elif(cadastrados[i][3] == "C"):
                print("\n\033[32m ~ Página dos Clientes ~\n\033[m")

                #Menu de escolha
                print("\033[32m ~ Menu de escolhas ~ \n 1-Atualizar Cadastro \n 2-Barra de Pesquisa \n 3-Deletar item do carrinho \n 4-Finalizar compra \n 5-Sair\033[m")
                escocli = int(input("\033[32m ➱ \033[m"))
                while(z):
                    if(escocli == 1):
                        for i in range(len(cadastrados)):
                            if(cadastrados[i][0] == email):
                                new = int(input("\n\033[32m ~ Digite o deseja modificar ~ \n 1-Email \n 2-Nome \n 3-Senha \n 4-Deletar Cadastro \n 5-Sair \n ➱ \033[m"))
                                while(new < 5):
                                    if(new == 1):
                                        newemail = str(input("\n\033[35m Digite seu novo email: \033[m")).lower()

                                        while not("@hotmail.com" in newemail or "@gmail.com" in newemail or "@outlook.com" in newemail) or newemail == email: 
                                            newemail = str(input("\033[31m Email inválido!!\033[m \n\n\033[35m Digite seu novo email: \033[m")).lower()
                                        
                                        cadastrados[i][0] = newemail  
                                    
                                    elif(new == 2):
                                        for j in range(len(cadastrados)):
                                            if(email == cadastrados[j][0] or newemail == cadastrados[j][0]):
                                                name = cadastrados[j][1].lower()
                                                newname = str(input("\n\033[35m Digite seu nome: \033[m")).lower()
                                                while(newname == "" or newname == name or newname.isnumeric()):
                                                    print("\033[31m Opção Inválida!! \n\033[m")
                                                    newname = str(input("\033[35m Digite seu nome: \033[m")).lower()
                                                cadastrados[j][1] = newname
                                    
                                    elif(new == 3):
                                        newsenha = str(input("\n\033[35m Digite sua senha contendo letras e números: \033[m"))
                                        for k in range(len(cadastrados)):
                                            if(email == cadastrados[k][0] or newemail == cadastrados[k][0]):
                                                while(newsenha.isalpha() or newsenha.isdigit() or newsenha == "" or newsenha == senha):
                                                    newsenha = str(input("\033[31m Senha inválida!! \033[m \n\n\033[35m Digite sua senha contendo letras e números: \033[m"))
                                                cadastrados[k][2] = newsenha

                                    elif(new == 4):
                                        excluir = input("\n\033[35m Tem certeza que deseja apagar sua conta? (s/n) \033[m").lower()
                                        while(excluir != "s" and excluir != "n"):
                                            print("\033[31m Valor Inválido!!\033[m") #cor
                                            excluir = input("\n\033[35m Tem certeza que deseja apagar sua conta? (s/n) \033[m").lower()
                                        if(excluir == "s"):
                                            for i in range(len(cadastrados)):
                                                if(email == cadastrados[i][0] or newemail == cadastrados[i][0]):
                                                    cadastrados.remove(cadastrados[i])
                                                    print("\033[31m Removido\033[m \n")
                                                    print(cadastrados, "\n")
                                                    login()

                                    print(cadastrados[i])

                                    new = int(input("\n\033[32m ~ Digite o deseja modificar ~ \n 1-Email \n 2-Nome \n 3-Senha \n 4-Deletar Cadastro \n 5-Sair \n ➱ \033[m"))

                        escocli = int(input("\n\033[32m ~ Menu de escolhas ~ \n 1-Atualizar Cadastro \n 2-Barra de Pesquisa \n 3-Deletar item do carrinho \n 4-Finalizar compra \n 5-Sair \n ➱ \033[m"))
                        
                    elif(escocli == 2):
                        h = True
                        while(h):
                                #Barra de Pesquisa
                                barra = input("\n\033[35m Digite o produto que deseja pesquisar: \033[m").upper()
                                j = True
                                for i in range(len(instrumentos)):
                                    if(len(barra) > 2):
                                        if(barra in instrumentos[i][0]):
                                            print(f" {instrumentos[i][0]}")
                                            j = False
                                        elif(len(instrumentos)-1 == i and j):
                                            print("\033[31m Produto não encontrado! \033[m \n")

                                        if(len(instrumentos)-1 == i and not(j)):
                                            opcao = str(input("\n\033[32m Desejar saber mais sobre algum desses instrumentos? (s/n) \033[m")).lower()
                                            if(opcao == "s"):
                                                pro = input("\033[35m\n Digite o nome do produto: \033[m").upper() 
                                                for i in range(len(instrumentos)):
                                                    if(pro == instrumentos[i][0] and "Esgotado" not in instrumentos[i]):
                                                        print(f"\033[36m\n Nome: {instrumentos[i][0]} \n Valor: {instrumentos[i][1]} \n Quantidade: {instrumentos[i][2]}\n Descrição: {instrumentos[i][3]} \n Fabricante: {instrumentos[i][4]} \n\033[m")
                                                        prod = instrumentos[i]


                                                        #Recomendação
                                                        print("\n\033[32m ~ Recomendações ~ \033[m")
                                                        for i in range(len(instrumentos)):
                                                            if(barra in instrumentos[i][0] and pro != instrumentos[i][0]):
                                                                print(f" {instrumentos[i][0]}")
                                                                print("")
                                                            
                                                        #carrinho
                                                        escocar = input("\nDeseja adicionar o item ao carrinho? (s/n) ").lower() #cor
                                                        while(escocar != "s" and escocar != "n"):
                                                            print("Opção Inválida!!") #cor
                                                            escocar = input("Deseja adicionar o item ao carrinho? (s/n)").lower()
                                                        if(escocar == 's'):
                                                            carrinho.append(prod)
                                                            print(carrinho)


                                                    elif(pro == instrumentos[i][0] and "Esgotado" in instrumentos[i]): 
                                                        print(f"\033[36m\n Nome: {instrumentos[i][0]} \n Valor: {instrumentos[i][1]}\033[m \n\033[31m Quantidade: Esgotado \033[m\n\033[36m Descrição: {instrumentos[i][3]} \n Fabricante: {instrumentos[i][4]} \n\033[m") 

                                                        #Recomendação
                                                        print("\033[32m\n ~ Recomendações ~ \033[m")
                                                        for i in range(len(instrumentos)):
                                                            if(barra in instrumentos[i][0] and pro != instrumentos[i][0]):
                                                                print(f" {instrumentos[i][0]}")
                                                                print("")
                                            elif(opcao == "n"):
                                                pass
                                            else:
                                                print("\033[31m Opção Inválida!!\033[m") 
                                    
                                    elif(len(instrumentos)-1 == i):
                                        print("\033[31m Opção Inválida!!\033[m")
                                
                                escocli = int(input("\n\033[32m ~ Menu de escolhas ~ \n 1-Atualizar Cadastro \n 2-Barra de Pesquisa \n 3-Deletar item do carrinho \n 4-Finalizar compra \n 5-Sair \n ➱ \033[m"))   
                                h = False
                                t = False
                    
                    elif(escocli == 3):
                        if(carrinho == []):
                            print("Nenhum item encontrado")
                        else:
                            print("Esse são seus itens do carrinho: ")
                            for c in carrinho:
                                print(c)
                            delcar = input("Qual o nome do produto que deseja deletar? ").upper()
                            for e in range(len(carrinho)):
                                if(carrinho[e][0] == delcar):
                                    carrinho.remove(carrinho[e])
                                    print("Instrumento deletado")
                                    r = False
                                    break
                                elif(e == len(carrinho)-1 and r):
                                    print("Item não encontrado!!")

                            print(carrinho)
                        escocli = int(input("\n\033[32m ~ Menu de escolhas ~ \n 1-Atualizar Cadastro \n 2-Barra de Pesquisa \n 3-Deletar item do carrinho \n 4-Finalizar compra \n 5-Sair \n ➱ \033[m")) 

                    elif(escocli == 4):
                        ender = input("Digite o endereço de entrega: ")
                        while(ender == ""):
                            print("Opção Inválida!!")
                            ender = input("Digite o endereço de entrega: ")
                        menufim = input("\n\033[32m ~ Forma de Pagamento ~ \n 1-Cartão \n 2-Boleto \n 3-Cancelar \n ➱ \033[m")
                        while(menufim != "1" and menufim != "2" and menufim != "3"):
                            print("Opção Inválida!!")
                            menufim = input("\n\033[32m ~ Forma de Pagamento ~ \n 1-Cartão \n 2-Boleto \n 3-Cancelar \n ➱ \033[m")
                        if(menufim == "1"):
                            if(carrinho != []):
                                cartnum = (input("Digite o número do Cartão: "))
                                while(not(cartnum.isnumeric()) or len(cartnum) != 16):
                                    print("Opção Inválida!!")
                                    cartnum = (input("Digite o número do Cartão: "))

                                cvc = (input("\nDigite o CVC: "))
                                while(not(cvc.isnumeric()) or len(cvc) != 3):
                                    print("Opção Inválida!!")
                                    cvc = (input("\nDigite o CVC: "))

                                data = (input("\nDigite a Data de Validade: "))
                                while(not(data.isnumeric()) or len(data) != 6):
                                    print("Opção Inválida!!")
                                    data = (input("\nDigite a Data de Validade: "))

                                cpf = (input("\nDigite o seu CPF: "))
                                while(not(cpf.isnumeric()) or len(cpf) != 11):
                                    print("Opção Inválida!!")
                                    cpf = (input("\nDigite o seu CPF: "))

                                print("\nEssa é a sua lista de compras ")
                                print(carrinho)
                                confirmvend = input("\nConfirmar Comprar: (s/n) ").lower()
                                while(confirmvend != "s" and confirmvend != "n"):
                                    print("Opção Inválida!!")
                                    confirmvend = input("Confirmar Comprar: (s/n) ").lower()
                                if(confirmvend == "s"):
                                    print("Compra Confirmada!")
                                    carrinho = []
                                    print("\nSeu carrinho foi atualizado ")
                                    print(carrinho)
                                elif(confirmvend == "n"): 
                                    print("Pedido cancelado")
                            else:
                                print("Carrinho Vazio")

                        elif(menufim == "2"):
                            pass
                        elif(menufim == "3"):
                            pass

                        escocli = int(input("\n\033[32m ~ Menu de escolhas ~ \n 1-Atualizar Cadastro \n 2-Barra de Pesquisa \n 3-Deletar item do carrinho \n 4-Finalizar compra \n 5-Sair \n ➱ \033[m"))

                    elif(escocli == 5):
                        escolhaLC = int(input("\n\033[32m Caso deseje fazer o Login digite (1). \n Caso deseje se Cadastrar digite (2). \n ➱ \033[m"))
                        logCad(escolhaLC)
                        

        if(i == len(cadastrados)-1 and f and t):
            print("\033[31m Informações incorretas!!\n\033[m")
            escolhaLC = int(input("\033[32m Caso deseje fazer o Login digite (1). \n Caso deseje se Cadastrar digite (2). \n ➱ \033[m"))
            logCad(escolhaLC)
            
def logCad(escolhaLC):
    if(escolhaLC == 1):
        login()
            
    else:
        email = str(input("\033[35m Digite seu email: \033[m"))
        while not("@hotmail.com" in email or "@gmail.com" in email or "@outlook.com" in email): 
            email = str(input("\033[31m Email inválido!!\033[m \n\033[35m Digite seu email: \033[m"))            

        nome = str(input("\033[35m Digite seu nome: \033[m"))

        senha = str(input("\033[35m Digite sua senha contendo letras e números: \033[m"))
        while (senha.isalpha() or senha.isdigit()):
            senha = str(input("\033[31m Senha inválida!! \033[m \n\033[35m Digite sua senha contendo letras e números: \033[m"))
        categoria = "C"

        usuario = [email, nome, senha, categoria]
        cadastrados.append(usuario)
        print(cadastrados)

        print("/033[32m Cadastro Concluido!\033[m")
        print("")
        login()
            
               
#MAIN

instrumentos = [["GUITARRAWOODSTOCK", 1017.9, 7, "Guitarra Woodstock Series TG-530 Preta", "Tagima", "Esgotado"], ["PIANO", 5241.5, 1, "Piano Digital Modelo P125B Preto", "Yamaha"], ["GUITARRATELECASTA", 2400.6, 3, "Guitarra Telecasta Series TC-530 Branco", "Yamaha"]]

cadastrados = [["adm@gmail.com", "adm", "adm123", "V"], ["patty@gmail.com", "patty", "321patty", "C"], ["robert@hotmail.com", "robert", "a123", "V"]]

while True:
        try:
            escolhaLC = int(input("\033[32m Caso deseje fazer o Login digite (1). \n Caso deseje se Cadastrar digite (2). \n ➱ \033[m"))
            if(escolhaLC == 1 or escolhaLC == 2):
                logCad(escolhaLC)
        except ValueError:
            print("\033[31m Opção Inválido!!\033[m")

