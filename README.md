# Dicionário de MongoDB


Esse diretório no gitHub foi uma ideia dada por alguns amigos meus para auxiliar as pessoas na 
matéria Banco de Dados II (Mongodb)<br>

Fontes de informações do dicionário de Mongo:<br>
Operadores: https://www.mongodb.com/pt-br/docs/manual/reference/operator/query/<br>
Update: https://www.mongodb.com/pt-br/docs/manual/reference/operator/update/ <br>
Métodos: https://www.mongodb.com/pt-br/docs/manual/reference/method/


Fontes de informações do dicionário de REDIS:<br>
Comandos: https://redis.io/docs/latest/commands/<br>
Estruturas de Dados que o Redis suport: https://redis.io/pt/redis-enterprise/estruturas-de-dados/



# Código do programa python:
```
from subprocess import Popen
from time import sleep
## Abrindo o Servidor
Popen(r'start cmd /K "cd C:\Program Files\MongoDB\Server\8.0\bin && mongod.exe"', shell=True)
sleep(5)

## Abrindo o MongoDB
Popen(r'start cmd /K "cd C:\mongo\mongosh-2.3.8-win32-x64\bin && mongosh.exe"', shell=True)
```
