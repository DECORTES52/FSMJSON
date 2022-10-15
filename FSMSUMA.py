libreria=[
    {
        'Estado Actual':0,
        'Entrada A':0,
        'Entrada B':0,
        'Salida':0,
        'Estado siguiente':0,
    },
    {
        'Estado Actual':0,
        'Entrada A':1,
        'Entrada B':0,
        'Salida':1,
        'Estado siguiente':0,
    },
    {
        'Estado Actual':0,
        'Entrada A':0,
        'Entrada B':1,
        'Salida':1,
        'Estado siguiente':0,
    },
    {
        'Estado Actual':0,
        'Entrada A':1,
        'Entrada B':1,
        'Salida':0,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Entrada A':1,
        'Entrada B':0,
        'Salida':0,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Entrada A':0,
        'Entrada B':1,
        'Salida':0,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Entrada A':1,
        'Entrada B':1,
        'Salida':1,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Entrada A':0,
        'Entrada B':0,
        'Salida':1,
        'Estado siguiente':0,
    },
    
]


import json

with open('libreria.json', 'w') as archivo:
    json.dump(libreria,archivo)

with open('libreria.json', 'r') as archivo:
    libreria_leida=json.load(archivo)
print(libreria_leida)
