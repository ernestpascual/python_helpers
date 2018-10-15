#####################
# by: ernestpascual #
####################

import json
import pandas as pd
from pymongo import MongoClient
from bson import json_util


print('Connecting..')
client = MongoClient('')
db =client['']
# Specify collection
collection = db['']

print('Reading csv..')
# Read csv
dump = pd.read_csv('')
dump_array = []


print ('Converting to json file..')
# convert pandas to json files
dump['json'] = dump.apply(lambda x: x.to_json(), axis=1)

print('Converting to bson..')
# convert to python objects for pymongo
for a in dump['json']:
    dump_array.append(json_util.loads(a))


# insert!
try:
    collection.insert_many(dump_array)
    print('Successful!')
except Exception as e:
    print(e)








