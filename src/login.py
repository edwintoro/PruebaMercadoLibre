from flask import Flask, render_template, request, redirect, url_for
import database as db


login = Flask(__name__)


@login.route("/login/<params>/<param>" )
def members(params,param):

    
    
    print(params,param)
    
    cursor = db.database.cursor()

    query = ("SELECT nombreUsuario FROM pruebamercadolibre.usuario "
         "WHERE nombreUsuario  %s AND %s")

    cursor.execute(query, (params, param))
    row = cursor.fetchone()
    if row  == None:
     return None
    else:
        print("eeeeee",row)
        return redirect(url_for("/members/<params>"))

 

















if __name__ == '__main__':
    
    
    login.run(debug=True)