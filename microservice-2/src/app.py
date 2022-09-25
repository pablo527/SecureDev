from flask import Flask, jsonify, request
from dbConnectClass import MongoDB

app = Flask(__name__)

@app.route('/insert-data', methods=['POST'])
def ping():
    request_data = request.get_json()
    print(request_data)
    
    mongoConnection = MongoDB();
    mongoConnection.connetTo('my_db','ips')
    
    mongoConnection.insertOneData(request_data)
    
    return jsonify({'reponse':'Data Insertada!'})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
