from flask import Flask, jsonify, request
import cuadro_controller_poo
from db_cuadros import create_tables
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/cuadros', methods=["GET"])
def get_cuadros():
    cuadros = cuadro_controller_poo.get_cuadros()
    cuadros_list=[]
    for cuadro in cuadros:
        elem = cuadro.serialize()
        cuadros_list.append(elem)
    return jsonify(cuadros_list)

@app.route("/cuadro/create", methods=["POST"])
def insert_cuadro():
    cuadro_details = request.get_json()
    id= cuadro_details["id"]
    title = cuadro_details["title"]
    author =cuadro_details["author"]
    price = cuadro_details["price"]
    creation = cuadro_details["creation"]
    movement = cuadro_details["movement"]
    material = cuadro_details["material"]
    result = cuadro_controller_poo.insert_cuadro(id,title,author,price,creation,movement,material)
    return jsonify(result)


@app.route("/cuadro/modify", methods=["PUT"])
def update_cuadro():
    cuadro_details = request.get_json()
    id = cuadro_details["id"]
    title = cuadro_details["title"]
    author =cuadro_details["author"]
    price = cuadro_details["price"]
    creation = cuadro_details["creation"]
    movement = cuadro_details["movement"]
    material = cuadro_details["material"]
    result = cuadro_controller_poo.update_cuadro(id,title,author,price,creation,movement,material)
    return jsonify(result)


@app.route("/cuadro/eliminate/<id>", methods=["DELETE"])
def delete_cuadro(id):
    result = cuadro_controller_poo.delete_cuadro(id)
    return jsonify(result)


@app.route("/cuadro/<id>", methods=["GET"])
def get_cuadro_by_id(id):
    cuadro = cuadro_controller_poo.get_by_id(id)
    return jsonify(cuadro)

@app.route("/cuadro/usd/<id>", methods=["GET"])
def get_cuadro_by_id_usd(id):
    cuadro = cuadro_controller_poo.get_by_id(id)
    xr = get_xr()
    price_usd = cuadro['price']/xr
    cuadro['price'] = round(price_usd,2)
    return jsonify(cuadro)

create_tables()

if __name__ == '__main__':
    app.run()