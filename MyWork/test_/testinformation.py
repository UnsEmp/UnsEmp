import requests
from flask import jsonify
import time


post_data = {
    'name': 'Alice',
    'hash': '',
    'method': 1
}
resp = requests.post('http://127.1.1.1:5000/', data=post_data)
print(resp.json())
