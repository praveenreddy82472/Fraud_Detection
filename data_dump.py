import pandas as pd
import json 
from pymongo import MongoClient, server_api
import certifi
ca = certifi.where()
client = MongoClient("mongodb+srv://tumatipraveenreddy23:Praveen987@cluster0.ghwmo.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
                             server_api=server_api.ServerApi('1'), tlsCAFile=ca)
DATA_FILE_PATH = "D:\Ineuron\Ml_projects\Fraud_Detection\Fraud_Detection.csv"
DATABASE_NAME = "Praveen"
COLLECTION_NAME = "Fraud"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")
    
    
     # Select the first 50,000 rows
    df = df.head(50000)
    print(f"Selected rows: {df.shape}")

    #Convert dataframe to json so that we can dump these record in mongo db
    df.reset_index(drop=True,inplace=True)

    json_record = list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    #insert converted json record to mongo db
    #client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    print("Inserted into MongoDB successfully!")
    
    
    
