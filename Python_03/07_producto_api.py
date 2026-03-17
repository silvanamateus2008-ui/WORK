import os
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

productos_db: list[dict] = []

class Producto:

    def __init__(self, id: int, nombre: str, precio: float):
        self.__id = id
        self.__nombre = nombre
        self.__precio = precio

    def actualizar_precio(self, nuevo_precio: float):
        self.__precio = nuevo_precio

    def to_dict(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "precio": self.__precio
        }

@app.route('/api/productos', methods=['GET'])
def listar_productos() -> tuple[Response, int]:
    return jsonify(productos_db), 200

@app.route('/api/productos', methods=['POST'])
def crear_producto() -> tuple[Response, int]:

    datos_entrantes: dict = request.get_json()

    if not datos_entrantes or "nombre" not in datos_entrantes or "precio" not in datos_entrantes:
        return jsonify({
            "error": "Faltan campos requeridos: nombre y precio"
        }), 400

    nuevo_producto = Producto(
        id=len(productos_db) + 1,
        nombre=datos_entrantes["nombre"],
        precio=datos_entrantes["precio"]
    )

    productos_db.append(nuevo_producto.to_dict())

    return jsonify({
        "mensaje": "Producto creado",
        "data": nuevo_producto.to_dict()
    }), 201

if __name__ == '__main__':

    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() == "true"
    port = int(os.getenv("PORT", 5000))

    app.run(host='0.0.0.0', port=port, debug=debug_mode)
