from flask import Flask, request
import threading
import time
import json

cpf_pesos = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
cnpj_pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

def valida_digito(num):
    if (num%11) < 2:
        return 0
    else:
        return 11 - (num%11)


def calcula_CPF(num):
    global cnpj_pesos

    resp = 0
    temp = 1

    for digit in num:

        resp += int(digit) * cpf_pesos[temp]
        temp += 1

    num += str(valida_digito(resp%11))

    resp = 0
    temp = 0

    for digit in num:
        resp += int(digit) * cpf_pesos[temp]
        temp += 1

    num += str(valida_digito(resp%11))

    return num

def calcula_CNPJ(num):
    global cnpj_pesos

    resp = 0
    temp = 1

    for digit in num:

        resp += int(digit) * cnpj_pesos[temp]
        temp += 1

    num += str(valida_digito(resp%11))

    resp = 0
    temp = 0

    for digit in num:
        resp += int(digit) * cnpj_pesos[temp]
        temp += 1

    num += str(valida_digito(resp%11))

    return num

app = Flask(__name__)

@app.route('/data', methods=['POST'])
def postData():

    response = []

    data = json.loads(request.get_json())

    print(f'received {len(data)} numbers to calculate')
    print(f'calculating...')

    for num in data:
        resp = None
        if len(num) == 9:
            resp = calcula_CPF(num)
        else:
            resp = calcula_CNPJ(num)
        
        response.append(resp)

    print(f'done!!')
    print(f'returning {len(data)} calculated numbers')

    return json.dumps(response)
