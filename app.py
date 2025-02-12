from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

# 📌 Conexión a la base de datos PostgreSQL
DATABASE_URL = "postgresql://postgres:Marcotest2025@localhost/listin"
conn = psycopg2.connect(DATABASE_URL)

@app.route('/buscar', methods=['GET'])
def buscar():
    nombre = request.args.get('nombre', '').strip().lower()

    if not nombre:
        return jsonify({"error": "Debe proporcionar un nombre"}), 400

    cur = conn.cursor()
    cur.execute("""
        SELECT nombre, puesto, telefono_movil, extension, telefono_fijo, correo_electronico 
        FROM empleados 
        WHERE LOWER(nombre) LIKE %s
    """, (f"%{nombre}%",))
    
    empleados = cur.fetchall()
    cur.close()

    if not empleados:
        return jsonify([])

    # Convertir resultados a JSON
    empleados_json = [
        {
            "Nombre empleado": emp[0],
            "Puesto": emp[1],
            "Teléfono móvil": emp[2],
            "Extensión": emp[3],
            "Telefono fijo": emp[4],
            "Correo Electrónico": emp[5]
        }
        for emp in empleados
    ]

    return jsonify(empleados_json)

if __name__ == '__main__':
    app.run(debug=True)



