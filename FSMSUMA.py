libreria=[
    {
        'Estado Actual':0,
        'Ent A':0,
        'Ent B':0,
        'Salida':0,
        'Estado siguiente':0,
    },
    {
        'Estado Actual':0,
        'Ent A':1,
        'Ent B':0,
        'Salida':1,
        'Estado siguiente':0,
    },
    {
        'Estado Actual':0,
        'Ent A':0,
        'Ent B':1,
        'Salida':1,
        'Estado siguiente':0,
    },
    {
        'Estado Actual':0,
        'Ent A':1,
        'Ent B':1,
        'Salida':0,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Ent A':1,
        'Ent B':0,
        'Salida':0,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Ent A':0,
        'Ent B':1,
        'Salida':0,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Ent A':1,
        'Ent B':1,
        'Salida':1,
        'Estado siguiente':1,
    },
    {
        'Estado Actual':1,
        'Ent A':0,
        'Ent B':0,
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
