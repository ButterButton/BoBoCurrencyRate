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
    result = DBSelect(db, DateTime)
    Json = ConvertToJson(DataSet(result))
    return Response(Json, mimetype='text/json')

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

def DBSelect(db, DateTime):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tw_bank WHERE Time = %s",(DateTime,))
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def DataSet(result):
    if(result == None):
        return None
    else:
        CurrencyRate = {
            "DateTime" : result[0][1],
            "ExchangeRate" : []
        }

        ExchangeRate = []

        for item in result:
            Currency = {}
            Currency["No"] = item[0]
            Currency["Currency"] = item[2]
            Currency["CashSell"] = item[3]
            Currency["CashBuy"] = item[4]
            Currency["SpotSell"] = item[5]
            Currency["SpotBuy"] = item[6]
            ExchangeRate.append(Currency)

        CurrencyRate["ExchangeRate"] = ExchangeRate

        return CurrencyRate

    return None

def ConvertToJson(DataSet):
    if(DataSet != None):
        return json.dumps(DataSet, ensure_ascii=False, indent=4)
    else:
        return None
if __name__ == "__main__":
    app.run(debug=True)