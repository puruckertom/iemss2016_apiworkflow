from beekeeper import API
import requests

resp = requests.get('http://qed.epa.gov/rest/ubertool/earthworm/').json()

wiki = API.from_hive_file('qed.epa.gov/api/#!/agdrift/get_rest_ubertool_agdrift.json')

uber = API.from_domain('qed.epa.gov/rest/ubertool/earthworm/', require_https=False)