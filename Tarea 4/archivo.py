import json
datos = '''
[
            {
        "Nombre":"Andres",
        "Edad":28,
        "Activo":71,
        "Saldo": 45
    },
    {
        "Nombre":"Alejandro",
        "Edad":28,
        "Activo":75,
        "Saldo": 45

    },
    {
        "Nombre":"Michelle",
        "Edad":29,
        "Activo":90,
        "Saldo": 45

    },
    {
        "Nombre":"Daniel",
        "Edad":27,
        "Activo":62,
        "Saldo": 45

    },
    {
        "Nombre":"Sofia",
        "Edad":30,
        "Activo":78,
        "Saldo": 45
    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":100,
        "Saldo": 45

    },
    {
        "Nombre":"Julian",
        "Edad":30,
        "Activo":70,
        "Saldo": 45
    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":100,
        "Saldo": 45

    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":100,
        "Saldo": 45

    },
    {
        "Nombre":"Jonathan",
        "Edad":29,
        "Activo":100,
        "Saldo": 45

    }
            ]'''
info = json.loads(datos)
print('Total usuarios:', len(info))
for elemento in info:\
print('Nombre', elemento['nombre'])
