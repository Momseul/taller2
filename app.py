import os
import platform
from flask import Flask
from jinja2 import Environment
from neas import Neas

# Jinja2 error
env = Environment()


system_info = platform.uname()
container_id = system_info.node
#container_id = os.uname()[1] 

app = Flask(__name__)

@app.route("/pokenea/json")
def pokenea_json():
    nea = Neas()
    json_pokenea = nea.mostrar_json(container_id)
    return json_pokenea

@app.route("/pokenea/imagen_frase")
def pokenea_imagen_frase():
    nea = Neas()
    container_id = platform.uname().node
    context = nea.mostrar_imagen_frase(container_id)

    if isinstance(context, dict):
        template = env.from_string("""
            <!DOCTYPE html>
            <html>
            <head>
                <title>Pokenea aleatorio</title>
            </head>
            <body>
                {% if context["imagen_codificada"] %}
                    <img src="data:image/png;base64,{{ context["imagen_codificada"] }}" alt="Imagen del pokenea aleatorio">
                {% else %}
                    <p>No hay imagen disponible</p>
                {% endif %}
                <p>{{ context["pokenea"]["frase_filosófica"] }}</p>
                <p>{{ context["pokenea"]["id"] }}</p>
                <p>ID del Contenedor: {{ context["container_id"] }}</p>
            </body>
            </html>
        """)
        return template.render(context=context)
    else:
        return context

if __name__ == "__main__":
    app.run(debug=True)
