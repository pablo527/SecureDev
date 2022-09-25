from flask import Flask, jsonify, request
from dbConnectClass import MongoDB
import requests


app = Flask(__name__)

@app.route('/', methods=['GET'])
def ping():    
    mongoConnection = MongoDB();
    mongoConnection.connetTo('my_db','ips')
    data = mongoConnection.getDataFromColection()
    blocksIps = []
    for r in data:
        print(r['block_ip'])
        blocksIps.append(r)
    
    listIps = requests.get('')
    
    filterIps = [i for i in listIps if i not in blocksIps]
    
    return jsonify({'reponse':'Data Consultada!', 'filterIps': filterIps})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5003, debug=True)
