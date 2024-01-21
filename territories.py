import requests
import pandas as pd
import configparser
from sqlalchemy import create_engine

config=configparser.ConfigParser()
config.read('config.ini')

postgres_config=config['postgres']
engine=create_engine(
    f"postgresql://{postgres_config['user']}:{postgres_config['password']}@{postgres_config['host']}/{postgres_config['database']}"
)

url=f'https://demodata.grapecity.com/northwind/api/v1/Territories'
response=requests.get(url)
data=response.json()
print(data)

df=pd.json_normalize(data)
df.to_sql('territories_raw',engine,if_exists='replace',index=False)
engine.dispose()