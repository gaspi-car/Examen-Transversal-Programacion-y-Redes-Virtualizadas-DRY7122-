import sqlite3
import hashlib
from flask import Flask, request

app = Flask(__name__)
db_name = 'usuarios.db'


@app.route('/')
def index():
    return 'Sitio web Examen Transversal DRY7122 - Item 3'


@app.route('/signup', methods=['POST'])
def signup():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS USUARIOS
                 (USERNAME TEXT PRIMARY KEY NOT NULL,
                  HASH TEXT NOT NULL);''')
    conn.commit()

    username = request.form['username']
    password = request.form['password']
    hash_value = hashlib.sha256(password.encode()).hexdigest()

    try:
        c.execute("INSERT INTO USUARIOS (USERNAME, HASH) VALUES ('{0}', '{1}')".format(username, hash_value))
        conn.commit()
    except sqlite3.IntegrityError:
        return "El usuario ya esta registrado."

    conn.close()
    return "Registro exitoso"


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT HASH FROM USUARIOS WHERE USERNAME = '{0}'".format(username))
    registro = c.fetchone()
    conn.close()

    if not registro:
        return "Usuario no encontrado"

    hash_ingresado = hashlib.sha256(password.encode()).hexdigest()

    if registro[0] == hash_ingresado:
        return "Login exitoso"
    else:
        return "Usuario o contrasena invalidos"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5800, ssl_context='adhoc')
