import pymongo
from flask import Flask, jsonify
from dbConnectClass import MongoDB
from datetime import date


app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():
    mongoConnection = MongoDB();
    mongoConnection.connetTo('my_db','ips')

    today = date.today()
    d1 = today.strftime("%d/%m/%Y")
    
    mongoConnection.insertOneData({'ip_bloqueada': '173.168.5.0', 'registry': d1})
    
    return jsonify({'reponse':'Data Insertada!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7072, debug=True)
