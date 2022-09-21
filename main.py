from flask import Flask
from flask_caching import Cache
import time
import asyncio
import aiohttp

urlDan = 'https://www.dan.me.uk/torlist/'
urlTorbu = 'https://check.torproject.org/torbulkexitlist'

results = ''

cache= Cache()

def create_app():
    app = Flask(__name__)
    app.config['CACHE_TYPE'] = 'simple'
    cache.init_app(app)
    return app

app = create_app()

@app.route('/getIp', methods=['GET'])
@cache.cached(timeout=1800)
def get_ip():
   start = time.time()
   asyncio.run(get_content())
   end = time.time()
   total_time = end - start
   print(total_time)
   print('You did it!')
   return results


def get_tasks(session):
    tasks = []
    tasks.append(session.get(urlDan.format(), ssl= False)) 
    tasks.append(session.get(urlTorbu.format(), ssl=False))
    return tasks

async def get_content():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        global results

        for response in responses:
            if response.status == 200:
                results += await response.text()