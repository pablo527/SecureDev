from flask import Flask
from flask_caching import Cache
import asyncio
import aiohttp
import os
import logging


urlDan = os.environ['URL_DAN']
urlTorbu = os.environ['URL_TOR']

results = ''

cache= Cache()

def create_app():
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'
    logging.basicConfig(filename='example.log',level=logging.DEBUG)
    cache.init_app(app)

    return app


app = create_app()

@app.route('/get', methods=['GET'])
@cache.cached(timeout=1800)
def get_ip():
   asyncio.run(get_content())
   return results.split('\n')
   

def get_tasks(session):
    tasks = []
    tasks.append(session.get(urlDan.format()))
    logging.info('consume url Dan') 
    tasks.append(session.get(urlTorbu.format()))
    return tasks

async def get_content():
    try:
        async with aiohttp.ClientSession() as session:
            tasks = get_tasks(session)
            responses = await asyncio.gather(*tasks)
            
            global results

            for response in responses:
                if response.status == 200:
                    results += await response.text()
    except:
        logging.info("An exception occurred") 




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['PORT'])                