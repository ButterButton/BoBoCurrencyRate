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
    return "HI Welcome to BoBo の CurrenyRate API"

@app.route("/QueryDateTime/<DateTime>")
def QueryDateTime(DateTime):
    db = inital()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tw_bank WHERE Time = %s",(DateTime,))
    result = cursor.fetchall()
    print(result[0][1])
    cursor.close()
    db.close()
    # JsonTransFormat(result)
    return DateTime

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

def JsonTransFormat(result):
    if(result == None):
        return None
    else:
        TempCurrencyRate = {
            "DateTime" : result[0][1],
            "ExchangeRate" : [
                {
                    "No" : 1,
                    "Currency" : "TWD",
                    "CashSell" : 123,
                    "CashBuy" : 456,
                    "SpotSell" : 798,
                    "SpotBuy" : 321
                }
            ]
        }
    return None

if __name__ == "__main__":
    app.run(debug=True)