import hashlib

while True:
    primeiro = str(input('Digite para conversao: '))

    xitao = hashlib.sha1(primeiro.encode())

    print(xitao.hexdigest())