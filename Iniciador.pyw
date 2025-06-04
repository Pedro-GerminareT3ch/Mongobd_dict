from subprocess import Popen
from time import sleep
## Abrindo o Servidor
Popen(r'start cmd /K "cd C:\Program Files\MongoDB\Server\8.0\bin && mongod.exe"', shell=True)
sleep(5)

## Abrindo o MongoDB
Popen(r'start cmd /K "cd C:\mongo\mongosh-2.3.8-win32-x64\bin && mongosh.exe"', shell=True)
 