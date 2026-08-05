import requests
def dish_fetch(num):
    response = requests.get(
        "https://api-colombia.com/api/v1/TypicalDish"
        )
    platos = response.json()
    if num < 0 or num >= len(platos):
          return {}
    return platos[num]

def main():
     response = requests.get(
          "https://api-colombia.com/api/v1/TypicalDish"
          )
     platos = response.json()

     print("=== MENÚ DE PLATOS TÍPICOS DE COLOMBIA ===")

     for i, plato in enumerate(platos):
          print(f"{i}. {plato['name']}")
          opcion = int(input("\nSeleccione un plato: "))
          plato = dish_fetch(opcion)
          if plato:
              print("\nNombre:", plato["name"])
              print("Descripción:", plato["description"])

if __name__ == "__main__":
     main()
