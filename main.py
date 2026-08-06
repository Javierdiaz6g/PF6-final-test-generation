import json
import requests


def dish_fetch(num):
    response = requests.get(
        "https://api-colombia.com/api/v1/TypicalDish"
        )
    platos = response.json()
    if num < 0 or num >= len(platos):      
          return{}
    plato = platos[num - 1]
    return {"id": plato['id'], "name": plato['name'], "description": plato['description']}


def main():
    while True:
        print("\n_________________________________________________________________________")
        print("\n|*< Bienvenidos al programa de Búsqueda de Platos Típicos de Colombia >*|")

        codigo = input("\n|*< Ingrese el código del plato (o escriba 'salir'):                > \n ")
        if codigo.lower() == "salir":
            print("👋 Gracias por usar el programa.")
            break
        elif not codigo.isdigit():
            print("❌ Por favor, ingrese un número válido.")
            continue
        num = int(codigo)
        print(f"|*< Buscando el plato con código {codigo}...                                 >*|\n")
        resultado = dish_fetch(num)
        print(f"|*< ID: {resultado['id']}                                                     ")
        print(f"|*< Nombre: {resultado['name']}                                               ")
        print(f"|*< Descripcion: {resultado['description']}                                     ")
if __name__=="__main__":
    main()