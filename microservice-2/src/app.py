from flask import Flask, jsonify, request
from dbConnectClass import MongoDB
import re

app = Flask(__name__)

@app.route('/insert-data', methods=['POST'])
def ping():
    request_data = request.get_json()
    ip = request_data['block_ip']
    
    ipv4_pattern = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    is_valid = re.match(ipv4_pattern, ip)

    if is_valid:
        mongoConnection = MongoDB();
        mongoConnection.connetTo('my_db','ips')
        mongoConnection.insertOneData(request_data)   
        return jsonify({'reponse':'data insert'}) 

    return jsonify({'reponse':'invalid'})     

    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
