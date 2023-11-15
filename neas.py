import random
import json
from base64 import b64encode
import requests

class Neas:
    def __init__(self):
        self.pokeneas = [
            {
                "id": 1,
                "nombre": "Juancho",
                "altura": 1.75,
                "habilidad": "Bailar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "La vida es una fiesta",
            },
            {
                "id": 2,
                "nombre": "Juana",
                "altura": 1.65,
                "habilidad": "Cantar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "El amor es la fuerza más poderosa del universo",
            },
            {
                "id": 3,
                "nombre": "Pedro",
                "altura": 1.85,
                "habilidad": "Pintar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "La belleza está en el ojo del que mira",
            },
            {
                "id": 4,
                "nombre": "Maluma",
                "altura": 1.85,
                "habilidad": "Cantar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "Mala mia",
            },
            {
                "id": 5,
                "nombre": "Feid",
                "altura": 1.70,
                "habilidad": "Cantar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "Ahora soy peor",
            },{
                "id": 6,
                "nombre": "Luisa",
                "altura": 1.70,
                "habilidad": "Actuar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "La vida es una lenteja",
            },
            {
                "id": 7,
                "nombre": "Fernando",
                "altura": 1.70,
                "habilidad": "Cocinar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "Ser o no ser",
            },
            {
                "id": 8,
                "nombre": "Mario",
                "altura": 1.70,
                "habilidad": "Enseñar",
                "imagen": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/987.png",
                "frase_filosófica": "Dios ha muerto",
            },
        ]

    def mostrar_json(self):
        pokenea = random.choice(self.pokeneas)
        datos_pokenea = {
            "id": pokenea["id"],
            "nombre": pokenea["nombre"],
            "altura": pokenea["altura"],
            "habilidad": pokenea["habilidad"],
        }
        json_pokenea = json.dumps(datos_pokenea)
        return json_pokenea

    def mostrar_imagen_frase(self):
        pokenea = random.choice(self.pokeneas)
        imagen_url = pokenea["imagen"]

        if imagen_url:
            response = requests.get(imagen_url)

            if response.status_code == 200:
                imagen_data = response.content
                imagen_codificada = b64encode(imagen_data).decode("utf-8")

                return {
                    "pokenea": pokenea,
                    "imagen_codificada": imagen_codificada,
                }
            else:
                return f"Error al obtener la imagen: {response.status_code}"
        else:
            return "No hay imagen disponible"
