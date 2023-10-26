from flask import Flask, redirect, url_for, jsonify
import requests
import database as db
import datetime




app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret" 
from flask_jwt import jwt, jwt_required, current_identity, JWTManager, create_access_token
jwt = JWTManager(app)


@app.route("/login/<params>/<param>" )
def login(params,param):

    print(params,param)
    cursor = db.database.cursor()
    query = ("SELECT nombreUsuario FROM pruebamercadolibre.usuario WHERE nombreUsuario = %s  AND password = %s ")
    tuple1 = (params, param)
    print(tuple1)
    cursor.execute(query,tuple1)
    row = cursor.fetchone()
    if row  == None:
     return ("not")
    else:
        print(row)
        token = create_access_token(identity=row)
        return jsonify(token=token)


@app.route("/members/<params>")
@jwt_required()
def members(params):
    url = 'https://restcountries.com/v3.1/name/'+ params +'?fullText=true'
    col = requests.get(url)
    return col.json()

@app.route("/membersIn/<params>", methods=["POST"])   
def membersInt(params):
    cursor = db.database.cursor()
    fecha = datetime.datetime.now()
    sql = "INSERT INTO pruebamercadolibre.riesgo (nombreRiesgo, pais, fechaModificacion) VALUES (%s, %s,%s)"
    val = ("bajo", "peru", fecha)
    cursor.execute(sql, val)
    db.database.commit()
    print(cursor.rowcount, "registro insertado")
    cursor.close()
    return cursor.rowcount


@app.route("/membersUp/<params>",methods=["POST"])   
def membersUp(params):
    cursor = db.database.cursor()
    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    cursor.execute(sql)
    db.database.commit()
    print(cursor.rowcount, "registro actualizado")
    cursor.close()
    return cursor.rowcount


@app.route("/membersDel", methods=["POST"])
def delete():
    cursor = db.database.cursor()
    sql = """Delete from Laptop where id = %s"""
    laptopId = 6
    cursor.execute(sql,(laptopId,))
    db.database.commit()
    print(cursor.rowcount, "registro eliminado")
    cursor.close()
    return cursor.rowcount

    
    

  
    
   
if __name__ == '__main__':
    
    
    app.run(debug=True)


