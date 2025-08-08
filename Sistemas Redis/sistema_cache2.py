import redis
import psycopg2
from os import system

# Conexão com Redis
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Conectar ao PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="BancoCache",
    user="postgres",
    password="1234"
)

tabela = "produtos"
key = "produtos"

def buscar_id():
    id_buscar = int(input("Insira o ID do produto desejado: "))
    produto = f"{key}:{id_buscar}"
    cursor = conn.cursor()

    if not r.exists(produto):
        print(f"Produto não encontrado no cache. Buscando no Banco...")
        cursor.execute(f"SELECT nome, preco FROM {tabela} where id = {id_buscar};")
        resultado = cursor.fetchone()
        if resultado:
            print(f"Armazenando o produto no cache com TTL de 60 segundos foi realizado")
            r.hset(produto, mapping={"nome":resultado[0], "preco":float(resultado[1])} ) 
            r.expire(produto, 60)
            hproduto = r.hgetall(produto)
            print(hproduto)
        else:
            print(f"O id {id_buscar} é inexistente no Banco. :V")
            pass
    else:
        hproduto = r.hgetall(produto)
        print(hproduto)
    input("")
    
def listar_produtos():
    cursor = 0
    encontrou = False
    
    while True:
        cursor, chaves = r.scan(cursor=cursor, match=f'{key}:*', count=100)
        for chave in chaves:
            valor = r.hgetall(chave)
            print(f"- {chave} | {valor}")
            encontrou = True
        if cursor == 0:
            break
    input("")
    
    
    
while True:
    system("cls")

    print("""--- MENU DE CONSULTAS DE PRODUTOS ---
1 - Buscar produto por ID
2 - Listar produtos em cache (Redis)
3 - Sair""")
    
    op = int(input("Escolha uma opção: "))
    if op == 1:
        buscar_id()

    if op == 2:
        listar_produtos()
        
    if op == 3:
        break
    
    
    