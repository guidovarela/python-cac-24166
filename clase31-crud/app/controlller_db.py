
# pip install pymysql
# pip freeze > requirements.txt


# conectar bbdd -> host, user, pass, db
import pymysql

host = "localhost"
user = "root"
clave= ""
db="tienda_py"


def conexionMySQL():
    return pymysql.connect(host=host,user=user,password=clave,database=db)

# consultas -> CRUD
