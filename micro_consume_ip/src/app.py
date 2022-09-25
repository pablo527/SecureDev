from flask import Flask
from flask_caching import Cache
import asyncio
import aiohttp
import os

urlDan = os.environ['URL_DAN']
urlTorbu = os.environ['URL_TOR']

results = ''

cache= Cache()

def create_app():
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)
    return app

app = create_app()

@app.route('/get', methods=['GET'])
@cache.cached(timeout=1800)
def get_ip():
   asyncio.run(get_content())
   return results


def get_tasks(session):
    tasks = []
    tasks.append(session.get(urlDan.format())) 
    tasks.append(session.get(urlTorbu.format()))
    return tasks

async def get_content():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        global results

        for response in responses:
            if response.status == 200:
                results += await response.text()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ['PORT'])                