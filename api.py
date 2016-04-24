#from beekeeper import API
import requests

#add ipynb for python3

url = 'http://qed.epa.gov/rest/ubertool/earthworm/'

resp = requests.get(url)

resp.status_code

resp.headers['content-type']

resp.encoding

resp.text

resp.json()