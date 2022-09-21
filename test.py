from urllib import response
from flask import Flask

from flask_caching import Cache
import time
import asyncio
import aiohttp
import requests



urlDan = 'https://www.dan.me.uk/torlist/'
urlTorbu = 'https://check.torproject.org/torbulkexitlist'
results = ''


def create_app():
    app = Flask(__name__)
    return app

app = create_app()

@app.route('/getIp', methods=['GET'])
def get_ip():
   start = time.time()
   global results
   response =  requests.get('https://www.dan.me.uk/torlist/')
   response = requests.get('https://check.torproject.org/torbulkexitlist')
   end = time.time()
   total_time = end - start
   print(total_time)
   print(response)
   print('You did it!')
   return response.text
