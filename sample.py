import xmltodict
import yaml
import json
from json import loads
from dicttoxml import dicttoxml

with open('sample.json','r') as f:
	jdata=json.load(f)
jdata=json.dumps(jdata)
xl=dicttoxml(loads(jdata)).decode("utf-8")
with open('sample.xml','w') as f:
	f.write(xl)
yam=yaml.safe_load(jdata)
with open ('sample.yml','w') as f:
	yaml.dump(yam,f)




