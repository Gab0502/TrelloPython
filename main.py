'''lista = [tempo desde o semeio, porcentagem de umidade solo, escola que cuida, nome do alimento, tempo desde ultima irrigação]'''

'''Lista com valores apropriados para cada verdura'''
alface = [31, 80, "alface"]
batata = [91, 70, "batata"]
cebolinha = [70, 60, "cebolinha"]
cenoura = [110, 60, "cenoura"]
tomatinho = [70, 70, "tomate cereja"]

'''Listas relacionadas as hortas das escolas e suas informações'''
alfacepramos = [22, 80, "Escola Cidade de anjos", "alface", 35]
batatapramos = [91, 70, "Escola Cidade de anjos", "batata", 12]
cenourapramos = [100, 50, "Escola Cidade de anjos", "cenoura", 14]

cenourapsonhos = [110, 60, "Escola Nova Era", "cenoura", 74]
cebolinhapsonhos = [50, 50, "Escola Nova Era", "cebolinha", 22]
alfacepsonhos = [31, 80, "Escola Nova Era", "alface", 10]

tomatinhopgomez = [40, 70, "Escola Estrela Guia", "tomate cereja", 7]
alfacepgomez = [5, 55, "Escola Estrela Guia", "alface", 23]
batatapgomez = [6, 80, "Escola Estrela Guia", "batata", 11 ]

'''funções'''

def check_produto(listaP,listaA):
    if listaP[0] < listaA[0]:
        print(f"Infelizmente ainda falta {listaA[0]-listaP[0]} dias para a proxima colheita, porem ainda temos diversos outros produtos!")
    else:
        print(f"Você está com sorte! O produto está disponivel na lojinha da {listaP[2]}, visite ela enquanto ainda temos o produto!")
    return

def checkresp(frase):
    resp = input(frase)
    while resp != "1" and resp != "2" and resp != "3" and resp!="4" and resp != "5":
        print("Desculpe, isso não é uma opção válida.")
        resp = input(frase)
    return resp

def checksair(frase):
    resp = input(frase)
    while resp != "voltar" and resp != "continuar":
        print("Desculpe, isso não é uma opção válida.")
        resp = input(frase)
    return resp

def checkescola(lista):
    print(f"Na {lista[2]} temos {lista[3]}, ele foi plantado a {lista[0]} dias e o solo esta com a umidade de {lista[1]}% no solo \n"
          f"e sua ultima irrigação foi a {lista[4]} minutos")
    return


def frasevegetal(lista):
    print(f"{lista[2]} é muito saudavel, demora cerca de {lista[0]} dias para ficar pronto para a colheita \n "
          f"e precisa com que o solo esteja com pelo menos {lista[1]}% de umidade no solo")

print("Bem-vindo à Horta Amiga")

endereco=input("Primeiramente digite seu endereço: ")

while True:
    '''menu de seleção de opções'''
    print("Digite o número para escolher uma opção:")
    home = checkresp("você deseja 1.ver produtos 2.saber sobre os vegetais 3. Saber onde doar 4.Detalhes tecnicos da horta ou deseja 5.sair? ")

    '''menu para produtos'''
    if home == "1":
        print("Você escolheu ver produtos.")
        while True:
            lugar = checkresp("Nosso projeto atualmente atua nas seguintes areas: \n"
                              "1.Parque Ramos 2.Parque dos Sonhos e 3.Parque Gomez, de qual lugar deseja ver produtos? ")
            if lugar == "1":
                produto=checkresp(f"Otima escolha, o parque Ramos é cuidada pela {alfacepramos[2]} e lá estão plantando: \n"
                                  f"1.Alface, 2.Batata e 3.Cenoura, qual deseja comprar?")
                if produto == "1":
                    check_produto(alfacepramos, alface)

                elif produto == "2":
                    check_produto(batatapramos,batata)

                else:
                    check_produto(cenourapramos, cenoura)

            elif lugar == "2":
                produto = checkresp(f"Otima escolha, o Parque dos Sonhos é cuidada pela {cenourapsonhos[2]} e lá estão plantando: \n"
                                    f"1.Cenoura, 2.Cebolinha e 3.Alface, qual deseja comprar?")
                if produto == "1":
                    check_produto(cenourapsonhos, cenoura)

                elif produto == "2":
                    check_produto(cebolinhapsonhos, cebolinha)

                else:
                    check_produto(alfacepsonhos, alface)

            else:
                produto = checkresp(f"Otima escolha, o Parque Gomez é cuidada pela {tomatinhopgomez[2]} e lá estão plantando: \n"
                                    f"1.Tomate Cereja, 2.Alface e 3.Batata, qual deseja comprar?")
                if produto == "1":
                    check_produto(tomatinhopgomez, tomatinho)

                elif produto == "2":
                    check_produto(alfacepgomez, alface)

                else:
                    check_produto(batatapgomez, batata)

            sair = checksair("Digite 'continuar' caso desejar ver mais produtos ou 'voltar' caso queira voltar para o HOME")

            if sair == "voltar":
                print("Tenta dar uma visita as escolas e parques para conhece-las melhor! Volte sempre!")
                break

            else:
                continue
            '''final do menu de produtos'''

            '''inicio informações sobre vegetais'''
    elif home == "2":

        print("Você escolheu saber sobre os vegetais e legumes.")
        while True:
            opcao = checkresp("Nós trabalhamos com diversos plantas, quais deseja saber mais sobre? \n"
                              "1.Alface, 2.Batata, 3.Cebolinha, 4.Cenoura, 5.Tomate Cereja")
            if opcao == "1":
                frasevegetal(alface)

            elif opcao == "2":
                frasevegetal(batata)

            elif opcao == "3":
                frasevegetal(cebolinha)

            elif opcao == "4":
                frasevegetal(cenoura)

            else:
                frasevegetal(tomatinho)

            sair = checksair("Esse foram fatos muito interessantes! \n"
                             "digite 'continuar' caso desejar ver mais  ou 'voltar' caso queira voltar para o HOME")

            if sair == "voltar":
                print("Os legumes e vegetais são alimentos otimos e muito necessarios para manter uma vida saudavel! Volte sempre!")
                break
            else:
                continue
                '''fim das informações de vegetais e legumes'''

    elif home == "3":
        print(f"Após verificar o seu endereço ({endereco}), as escolas mais proximas são {alfacepramos[2]}, {alfacepsonhos[2]}, {alfacepgomez[2]}\n"
              f"O seu lixo organico poderá ser doado para elas diretamente, você terá de dizer seu cpf para que ganhe pontos para descontos nos produtos vendidos nas lojas \n"
              f"O lixo organico doado será transformado em adubo que será utilizado nas hortas! Muito obrigado pela sua contribução")


    elif home == "4":
        while True:
            print("Você escolheu saber detalhes tecnicos de cada horta")
            opcao = checkresp("De qual escolinha deseja saber sobre a horta? 1.Escola Cidade de anjos 2.Escola Nova Era 3.Escola Estrela Guia")
            
            if opcao=="1":
                checkescola(alfacepramos)
                checkescola(batatapramos)
                checkescola(cebolinhapsonhos)
            elif opcao=="2":
                checkescola(cenourapsonhos)
                checkescola(cebolinhapsonhos)
                checkescola(alfacepsonhos)
            else:
                checkescola(tomatinhopgomez)
                checkescola(alfacepgomez)
                checkescola(batatapgomez)

            sair = checksair("digite 'continuar' caso desejar ver mais  ou 'voltar' caso queira voltar para o HOME")

            if sair == "voltar":
                print("Os legumes e vegetais são alimentos otimos e muito necessarios para manter uma vida saudavel! Volte sempre!")
                break
            else:
                continue

    elif home == "5":
        print("Você escolheu a opção sair, muito obrigado por usar nossos serviços, até mais!!")
        break

