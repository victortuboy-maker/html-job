from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'travelagency'

mysql = MySQL(app)

@app.route("/products")
def get_products():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products")
    data = cur.fetchall()
    return jsonify(data)

@app.route("/register", methods=["POST"])
def register():
    data = request.json
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name,email,password) VALUES(%s,%s,%s)",
                (data['name'], data['email'], data['password']))
    mysql.connection.commit()
    return jsonify({"message":"User registered"})

if _name_ == "_main_":
    app.run(debug=True)