from flask import Flask, request, jsonify
import pandas as pd
from flask_cors import CORS  # Importar CORS

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Cargar el archivo Excel
FILE_PATH = "Listin.xlsx"
df = pd.read_excel(FILE_PATH)

@app.route('/buscar', methods=['GET'])
def buscar():
    nombre = request.args.get('nombre', '').strip().lower()

    if not nombre:
        return jsonify({"error": "Debe proporcionar un nombre para buscar"}), 400

    # Filtrar los resultados
    resultados = df[df['Nombre empleado'].str.lower().str.contains(nombre, na=False)]

    if resultados.empty:
        return jsonify([])  # Si no hay resultados, devolver una lista vacía

    return jsonify(resultados.to_dict(orient="records"))  # Enviar todos los datos

if __name__ == '__main__':
    app.run(debug=True)

