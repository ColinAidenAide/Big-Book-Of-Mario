from flask import Flask
from requests import get

app = Flask(__name__)
SITE_NAME = 'https://https://sites.google.com/colf.edu.ph/thebigbookofsupermariowiki'

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    return get(f'{SITE_NAME}/{path}').content

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
