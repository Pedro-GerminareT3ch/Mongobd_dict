import redis
from os import system

# Conexão com Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

def create_config():
    chave = input("Nome da configuração: ")
    if r.exists(f"config:{chave}"):
        print("Uma configuração com esse nome já existe. Criação interrompida. :V")
    else:
        valor = input("Valor da configuração: ")
        r.set(f"config:{chave}", valor)
        print("Configuração criada com sucesso.")
        print(f"- config:{chave} | {valor}")
    input("")

def list_config():
    cursor = 0
    encontrou = False
    
    while True:
        cursor, chaves = r.scan(cursor=cursor, match='config:*', count=100)
        for chave in chaves:
            valor = r.get(chave)
            print(f"- {chave} | {valor}")
            encontrou = True
        if cursor == 0:
            break
    input("")

def update_config():
    chave = input("Nome da chave a ser atualizada: ")
    if r.exists(f"config:{chave}"):
        novo_valor = input("Insira o novo valor para a chave: ")
        r.set(f"config:{chave}", novo_valor)
        print(f"A configuração de '{chave}' foi atualizada com sucesso.")
    else: 
        print(f"A chave de nome 'config:{chave}' não existe. :V")
    input("")        
        
def remove_config():
    chave = input("Nome da configuração a ser removida: ")
    if r.exists(f"config:{chave}"):
        r.delete(f"config:{chave}")
        print(f"A chave de nome 'config:{chave}' foi deletada com sucesso")
    else:
        print(f"A chave de nome 'config:{chave}' é inexistente. :V")
    input("")

while True:
    print("""---MENU DE CONFIGURAÇÕES---
1 - Criar nova configurações
2 - Listar todas as configurações
3 - Atualizar uma configuração
4 - Remover uma configuração
5 - Sair
""")
    op = int(input("> "))    
    
    if op == 1:
        create_config()
        system("cls")
        
    if op == 2:
        list_config()
        system("cls")
    
    if op == 3:
        update_config()
        system("cls")
        
    if op == 4:
        remove_config()
        system("cls")
    
    if op == 5:
        print("Saindo...")
        break