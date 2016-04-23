from beekeeper import API

wiki = API.from_hive_file('qed.epa.gov/api/#!/agdrift/get_rest_ubertool_agdrift.json')

uber = API.from_domain('http://qed.epa.gov/api/#!/agdrift/get_rest_ubertool_agdrift', require_https=False)