from flask import Flask
from flaskext.mysql import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret_key"
app.config['MYSQL_DATABASE_HOST'] = 'mysql'
app.config['MYSQL_DATABASE_USER'] = 'baris'
app.config['MYSQL_DATABASE_PASSWORD'] = '1'
app.config['MYSQL_DATABASE_DB'] = 'SuadiyeDB'
app.config['MYSQL_DATABASE_PORT'] = 3306

db = MySQL()
db.init_app(app)


@app.route("/")
def index():
    cursor = db.get_db().cursor()
    query = "Select * from Furniture"
    cursor.execute(query)

    liste = {}

    for i in cursor:
        liste['FurnitureName'] = i[1]
        liste['FurnitureImage'] = i[2]

    cursor.close()

    return liste


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
