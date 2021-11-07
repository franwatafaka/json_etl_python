# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
from json.decoder import JSONDecodeError

file = 'mi_json.json'

def serializar():
    print("Funcion que genera un archivo JSON")
    # JSON Serialize
    # Armar un JSON que represente los datos personales
    # de su persona (puede invitar los datos sino quiere exponer
    # información confidencial)

    # Debe armar un JSON que tenga como datos
    # nombre, apellido, DNI
    # Dentro debe tener una lista donde coloque cantidad de elementos de vestir
    # ejemplo -->
    #  { "prenda": "zapatilla", "cantidad": 4 }
    #  { "prenda": "remeras", "cantidad": 12 }
    # Que su lista de prendas dentro del JSON tenga al menos 2 prendas

    # json_data = {...}
    json_data = {
        "nombre": "Fracisco",
        "apellido": "Sosa",
        "Vestimenta":[
        { "prenda": "zapatilla", "cantidad": 2 },
        { "prenda": "remeras", "cantidad": 4 },
        { "prenda": "camisas", "cantidad": 4 },
        { "prenda": "jeans", "cantidad": 5 },
        ]
    }
    # Una vez que finalice el JSON realice un "dump" para almacenarlo en
    # un archivo que usted defina
    print('Imprimir json como un objeto')
    print(json_data)
    # Observe el archivo y verifique que se almaceno lo deseado
    with open(file, 'w') as jsonfile:
        data = [json_data]
        json.dump(data, jsonfile, indent=4)
    print('Imprimo el archivo')
    print(json.dumps(data, indent=4))
    print('Funcion serialize finalizó')

def deserializar():
    print("Funcion que lee un archivo JSON")
    # JSON Deserialize
    # Basado en la función  anterior debe abrir y leer el contenido
    # del archivo y guardarlo en un objeto JSON utilizando el método
    # load()

    nvo_json = {}
    with open(file, 'r') as jsonfile:
        nvo_json = json.load(jsonfile)
    
    # Luego debe convertir ese JSON data en json_string utilizando
    # el método "dumps" y finalmente imprimir en pantalla el resultado
    with open('mi_json.json', 'w') as jsonfile:
        json.dump(nvo_json,jsonfile, indent=4)
    # Recuerde utilizar indent=4 para poder observar mejor el resultado
    # en pantalla y comparelo contra el JSON que generó en la función anterior
    print('Imprimo el archivo deserializado')
    print(json.dumps(nvo_json, indent=4))

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    serializar()
    deserializar()

    print("terminamos")
