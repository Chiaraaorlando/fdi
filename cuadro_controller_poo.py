from db_cuadros import get_db
from clase_cuadro import Cuadro


def insert_cuadro(id, title, author, price, creation, movement, material):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO cuadros (id, title, author, price, creation, movement, material) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?)"
    cursor.execute(statement, [id, title, author, price, creation, movement, material])
    db.commit()
    return True

def update_cuadro(id, title, author, price, creation, movement, material):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE cuadros SET title = ?, author = ?, price= ?, creation= ?, movement= ?, material= ? \
    WHERE id = ?"
    cursor.execute(statement, [title, author, price, creation, movement, material, id])
    db.commit()
    return True


def delete_cuadro(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM cuadros WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, title, author, price, creation, movement, material FROM cuadros WHERE id = ?"
    cursor.execute(statement, [id])
    single_cuadro = cursor.fetchone()
    id = single_cuadro[0]
    title = single_cuadro[1]
    author = single_cuadro[2]
    price = single_cuadro[3]
    creation = single_cuadro[4]
    movement = single_cuadro[5]
    material = single_cuadro[6]
    cuadro = Cuadro(id,title, author, price, creation, movement, material)
    return cuadro.serialize_details()


def get_cuadros():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, title, author, price, creation, movement, material FROM cuadros"
    cursor.execute(query)
    cuadro_list = cursor.fetchall()
    list_of_cuadros=[]
    for cuadro in cuadro_list:
        id = cuadro[0]
        title = cuadro[1]
        author = cuadro[2]
        price = cuadro[3]
        creation= cuadro[4]
        movement = cuadro[5]
        material = cuadro[6]
        cuadro_to_add = Cuadro(id,title, author, price, creation, movement, material)
        list_of_cuadros.append(cuadro_to_add)
    return list_of_cuadros