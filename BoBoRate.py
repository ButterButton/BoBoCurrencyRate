from flask import Flask
from flask import Response
import datetime
import json
import mysql.connector
import configparser
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    db = inital()
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM tw_bank LIMIT 10""")
    result = mycursor.fetchall()
    print(result)
    cursor.close()
    db.close()
    return "HI"

def inital():
    configfile = configparser.ConfigParser()
    configfile.read("config.py")
    mydb = mysql.connector.connect(
        host = configfile["DB"]["D_host"],
        port = configfile["DB"]["D_port"],
        user = configfile["DB"]["D_user"],
        passwd = configfile["DB"]["D_passwd"],
        database = configfile["DB"]["D_name"]
        )
    return mydb
    # mycursor = mydb.cursor()
    # mycursor.execute("""SELECT * FROM tw_bank LIMIT 10""")
    # result = mycursor.fetchall()
    # print(result)
    # mycursor.close()
    # mydb.close()
    return mycursor

if __name__ == "__main__":
    app.run(debug=True)