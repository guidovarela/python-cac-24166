# pip install pymysql
# pip freeze > requirements.txt
# pip install -r requirements.txt
# conectar bbdd -> host, user, pass, db

import pymysql

# local -> wamp
# host = "localhost"
# user = "root"
# clave= ""
# db="tienda_py"

# remota -> pythonenaywhere
host = "guidovarela.mysql.pythonanywhere-services.com"
user = "guidovarela"
clave= "codo2024"
db="guidovarela$tienda-py"

def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)
