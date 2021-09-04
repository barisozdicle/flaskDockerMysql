from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = "baris"


@app.route("/")
def index():
    db = mysql.connector.connect(user='baris', password='1',
                                 host='mysql', port=3306, database='SuadiyeDB')

    cursor = db.cursor()
    query = "Select * from Furniture"
    cursor.execute(query)

    liste = {}

    for i in cursor:
        liste['FurnitureName'] = i[1]
        liste['FurnitureImage'] = i[2]

    cursor.close()
    db.close()

    return liste


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
