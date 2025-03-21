from flask import Flask
from flaskext.mysql import MySQL
import time
import sys
import os

def configure_app(app):
    config_mapping = {
        'SECRET_KEY': 'APP_SECRET_KEY',
        'MYSQL_DATABASE_HOST': 'MYSQL_HOST',
        'MYSQL_DATABASE_USER': 'MYSQL_USER',
        'MYSQL_DATABASE_PASSWORD': 'MYSQL_PASSWORD',
        'MYSQL_DATABASE_DB': 'MYSQL_DATABASE',
        'MYSQL_DATABASE_PORT': ('MYSQL_PORT', int, 3306),  # (env_key, type_cast, default_value)
    }
    
    for config_key, env_data in config_mapping.items():
        if isinstance(env_data, tuple):
            env_key, type_cast, default = env_data
            app.config[config_key] = type_cast(os.environ.get(env_key, default))
        else:
            app.config[config_key] = os.environ.get(env_data)

app = Flask(__name__)
configure_app(app)

db = MySQL()
db.init_app(app)

# MySQL bağlantısını kontrol et
max_tries = 30  # 30 deneme (5 dakika)
while max_tries > 0:
    try:
        conn = db.connect()
        if conn:
            print("MySQL bağlantısı başarılı!")
            conn.close()
            break
    except Exception as e:
        print(f"MySQL'e bağlanılamıyor, {max_tries} deneme kaldı...")
        max_tries -= 1
        time.sleep(10)  # 10 saniye bekle

if max_tries <= 0:
    print("MySQL'e bağlanılamadı, uygulama kapatılıyor.")
    sys.exit(1)

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
    debug = os.environ.get('FLASK_DEBUG', '0') == '1'
    app.run(debug=debug, host="0.0.0.0", port=int(os.environ.get('CONTAINER_FLASK_PORT', 5000)))
