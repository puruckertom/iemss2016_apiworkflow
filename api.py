#from beekeeper import API
import requests

#add ipynb for python3

url_qed = 'http://qed.epa.gov/rest/ubertool/earthworm/'
url_ncrs = 'https://alm.engr.colostate.edu/cb/report/10136'
url_storet = 'https://www3.epa.gov/storet/web_services.html'
url_nwis = 'http://qwwebservices.usgs.gov/'
url_epa = 'https://developer.epa.gov/category/api/'

resp = requests.get(url)

resp.status_code

resp.headers['content-type']

resp.encoding

resp.text

resp.json()
