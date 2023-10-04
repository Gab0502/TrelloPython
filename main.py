import json

def forcaInput(frase,lista):
    opcao = int(input(frase))
    while opcao not in lista:
        opcao = int(input(frase))
    return opcao

def salvar():
    with open("data.json","w") as json_file:
        json.dump(trello, json_file)
def printDic(dic):
    for key in dic.keys():
        print(f"{key} : {dic[key]['Nome']}")
    return
def printaDicFull(dic):
    for key in dic.keys():
        if type(dic[key]) is dict:
            printaDicFull(dic[key])
        else:
            print(f"{key} : {dic[key]}")
    return
trello = {}
arquivo='data.json'
try:
    with open(arquivo,"r") as json_file:
        trello = json.load(json_file)


except FileNotFoundError:
    print('Nenhum dado encontrado')
else:
    print('dados carregados')

i=len(trello)
print("Bem vindo ao trello.py")

while True:

    print(f' \n Você tem {i} tarefas \n')
    printDic(trello)

    acao=forcaInput("Deseja fazer o que? 1.Adicionar Tarefa 2.Remover Tarefa 3.Ver Tarefa 4.Sair e Salvar", [1,2,3,4])

    if acao==1:
        i+=1
        print("Certo, vamos começar")
        trello[i]={}
        trello[i]['Nome']=input("Digite o nome da tarefa: ")
        trello[i]['Membro(s) Responsavel'] = input('Digite o nome do membro responsavel pela tarefa: ')
        trello[i]['data'] = input("Digite a data de entrega: ")
        trello[i]['descrição'] = input("Digite a descrição da tarefa: ")
        trello[i]['status'] = input('Digite como está o progresso da tarefa')
        trello[i]['comentarios'] = {}

    elif acao==3:
        tarefa=forcaInput('Qual tarefa deseja ver?', trello.keys())
        printaDicFull(trello[tarefa])
        opcao=forcaInput('Deseja adicionar um comentario? 1- sim 2- não', [1,2])
        if opcao == 1:
            nome = input('Digite seu nome')
            trello[tarefa]['comentarios'][nome]=input('Digite seu comentario')
        else:
            continue
    else:
        salvar()
        break
