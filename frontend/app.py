# app.py (en el directorio del proyecto)
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def load_model(model_name):
    """Carga y devuelve el modelo descargado."""
    try:
        url = f"https://huggingface.co/models/{model_name}" # Cambia si es diferente
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si hay un error en la solicitud
        return response.json()['object']  # Ajusta según el formato de la respuesta del modelo
    except Exception as e:
        print(f"Error al cargar el modelo: {e}")
        return None

model_name = "bert-base-uncased" # Reemplaza con el nombre del modelo que quieres usar.
model = load_model(model_name)

if model is not None:
    def predict(prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Ajusta según el modelo que usas
                prompt=prompt,
                max_tokens=150,
                n_blast=5 # Número de resultados de la respuesta (ajusta)
            )
            return response.choices[0].text
        except Exception as e:
             print(f"Error al predecir: {e}")
             return "No se pudo generar una respuesta."

    # Ejemplo de uso en el frontend
    prompt = request.args.get('prompt')  # Obtener el prompt del usuario desde la URL
    if prompt:
        prediction = predict(prompt)
        return prediction
    else:
        return "Por favor, ingresa un prompt."

if __name__ == '__main__':
    app.run(debug=True)
#