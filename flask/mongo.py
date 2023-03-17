import pymongo
import pandas as pd
from bson import json_util
import json 

def getDisease():
    client = pymongo.MongoClient(
    'mongodb+srv://Preet:Preet1$A@cluster0.xpb6hhy.mongodb.net/?retryWrites=true&w=majority')
    db = client['test']
    collections = db['symptoms']
    allDocs = collections.find()
    allDocs = json.loads(json_util.dumps(allDocs))
    lst = list(allDocs)
    df = pd.DataFrame(lst)
    # print(df)
    return df
getDisease()
