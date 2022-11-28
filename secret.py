import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()
cluster = os.getenv('CLUSTER')
client = MongoClient(cluster)
db = client["Lisence"]
data = db.user_data
admin = db.lisences
