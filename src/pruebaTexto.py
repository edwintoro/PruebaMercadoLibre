from flask import Flask, jsonify
import requests
import database as db
import datetime
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from json import JSONEncoder
import json
from flask import Flask, request, jsonify


app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret" 


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
        value = {
        "nombre": row
        }
        print("tttttt",value)
        #token = create_access_token(identity= {"name":"Hello", "age":35} )
        #print(token)
        cursor.close()
   
        return  json.dumps(value)


@app.route("/members/<params>")
#@jwt_required()
def members(params):
    url = 'https://restcountries.com/v3.1/name/'+ params +'?fullText=true'
    col = requests.get(url)
    return col.json()

@app.route("/membersIn", methods=["POST"])   
def membersInt():
    print("content1")
    nombreRiesgo = request.json['nombreRiesgo']
    pais = request.json['pais']
    codigo = request.json['codigo']
    divisa = request.json['divisa']
    idioma = request.json['idioma']
    ciudad_Capital = request.json['ciudad_Capital']
    codigo_llamada = request.json['codigo_llamada']
    region = request.json['region']
    sub_region = request.json['sub_region']
    impacto = request.json['impacto']
    probabilidad = request.json['probabilidad']
    

    print("content3")

    cursor = db.database.cursor()
    fecha = datetime.datetime.now()
    sql = "INSERT INTO pruebamercadolibre.riesgo ( nombreRiesgo, pais, fechaModificacion,  codigo,  divisa, idioma, ciudad_Capital, codigo_llamada, region, sub_region, impacto, probabilidad) VALUES (%s, %s,%s)"
    val = (nombreRiesgo,pais,fecha,codigo,divisa,idioma,ciudad_Capital,codigo_llamada,region,sub_region,impacto,probabilidad)
    cursor.execute(sql, val)
    db.database.commit()
    print(cursor.rowcount, "registro insertado")
    cursor.close()
   
    return 'test'  # cursor.rowcount




@app.route("/membersUp/<params>/<param>",methods=["POST"])   
def membersUp(params, param):
    cursor = db.database.cursor()
    sql = "UPDATE pruebamercadolibre.riesgo SET nombreRiesgo = %s  AND idRiesgo = %s "
    tuple1 = (params, param)
    cursor.execute(sql,tuple1)
    db.database.commit()
    print(cursor.rowcount, "registro actualizado")
    cursor.close()
    return cursor.rowcount


@app.route("/membersDel<params>", methods=["POST"])
def delete(params):
    cursor = db.database.cursor()
    sql = """Delete from pruebamercadolibre.riesgo where idRiesgo = %s"""
    updateId = params
    cursor.execute(sql,updateId)
    db.database.commit()
    print(cursor.rowcount, "registro eliminado")
    cursor.close()
    return cursor.rowcount



@app.route("/riesgoGet" )
def riesgoGet():


    cursor = db.database.cursor()
    query = ("SELECT FROM pruebamercadolibre.riesgo ")
   
    print("paso")
    cursor.execute(query)
    print("paso1")
    row = cursor.fetchall()
    print("row",row)
    if row  == None:
     return ("not")
    else:
        value = {
        "data": row
        }
        print("tttttt",value)
        #token = create_access_token(identity= {"name":"Hello", "age":35} )
        #print(token)
        cursor.close()
   
        return  json.dumps(value)
    

@app.route("/riesgoGet/<param>" )
def riesgoGetParam(param):


    cursor = db.database.cursor()
    query = ("SELECT FROM pruebamercadolibre.riesgo where nombreRiesgo LIKE %s ")
    valor = (param)
    print("paso222333")
    cursor.execute(query,param)
    print("paso7575757")
    row = cursor.fetchall()
    print("row",row)
    if row  == None:
     return ("not")
    else:
        value = {
        "data": row
        }
        print("vvvvv",value)
        #token = create_access_token(identity= {"name":"Hello", "age":35} )
        #print(token)
        cursor.close()
   
        return  json.dumps(value)
    
    
   
if __name__ == '__main__':
    
    
    app.run(debug=True)


