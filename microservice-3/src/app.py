from flask import Flask, jsonify
from dbConnectClass import MongoDB
import ast
import asyncio
import aiohttp
import os


app = Flask(__name__)
@app.route('/', methods=['GET'])
def ping():  
    mongoConnection = MongoDB()
    mongoConnection.connetTo('my_db','ips')
    data = mongoConnection.getDataFromCollection()
    blocksIps = []
    for r in data:
        blocksIps.append(r['block_ip'])
    
    results = asyncio.run(get_content())
    output = ast.literal_eval(results)
    filterIps = [i for i in output if i not in blocksIps]
    del results
    return jsonify({'reponse':'Data Consultada!', 'filterIps': filterIps})



def get_tasks(session):
    url = os.environ['URL_SERVICE']
    tasks = []
    tasks.append(session.get(url.format())) 
    return tasks

async def get_content():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        print(responses[0])
        print("HELLOO")
  
        for response in responses:
            results= await response.text()
            return results

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=os.environ['PORT'])
