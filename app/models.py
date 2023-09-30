from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os

load_dotenv()
mongo_password = os.getenv("MONGO_SECRET")
mongo_user = os.getenv("MONGO_USER")

uri = f"mongodb+srv://{mongo_user}:{mongo_password}@whatsappdictionary.e3u6ak7.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

dictionary_collection = client['MY_DB']['dictionary']

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)