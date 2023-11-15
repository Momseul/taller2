from flask import Flask, render_template
from jinja2 import Environment
from neas import Neas

# Create a Jinja2 environment and register the custom filter
env = Environment()

app = Flask(__name__)

@app.route("/pokenea/json")
def pokenea_json():
    nea = Neas()
    json_pokenea = nea.mostrar_json()
    return json_pokenea

@app.route("/pokenea/imagen_frase")
def pokenea_imagen_frase():
    nea = Neas()
    context = nea.mostrar_imagen_frase()

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
            </body>
            </html>
        """)
        return template.render(context=context)
    else:
        return context

if __name__ == "__main__":
    app.run(debug=True)
