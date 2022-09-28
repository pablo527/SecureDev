from flask import Flask, jsonify, request
from dbConnectClass import MongoDB
import re
import logging


app = Flask(__name__)

logging.basicConfig(filename='example.log',level=logging.DEBUG)


@app.route('/insert-data', methods=['POST'])
def ping():
    try:
        request_data = request.get_json()
        ip = request_data['block_ip']
        is_valid = valid_ip(ip)
        
        if is_valid:
            mongoConnection = MongoDB();
            mongoConnection.connetTo('my_db','ips')
            mongoConnection.insertOneData(request_data)   
            return jsonify({'reponse':'data insert'}) 

        return jsonify({'reponse':'invalid'})   
    except: 
        print("An exception occurred")     

def valid_ip(ip):

    ipv4_pattern = "^(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
    ipv6_pattern = '^(([0-9a-fA-F][0-9a-fA-F]{0,3}:){7}([0-9a-fA-F][0-9a-fA-F]{0,3}){1})$'
    
    if re.match(ipv4_pattern, ip) or re.match(ipv6_pattern,ip):
        return True
    else:
        return False    
    

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
