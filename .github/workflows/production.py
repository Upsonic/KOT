import os
import requests
import time
from kot import KOT_Remote
from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")

webhook = os.environ.get("PRODUCTION_WEBHOOK")
tag = os.environ.get("PRODUCTION_TAG")
access_keys = os.environ.get("PRODUCTION_ACCESS_KEYS")

try:
  response = requests.request("POST", f"{webhook}?SERVICE_TAG={tag}", verify=False)
  
  
  time.sleep(50)
  
  
  server = os.environ.get("PRODUCTION_SERVER")
  password = os.environ.get("PRODUCTION_SERVER_PASS")
  cloud = KOT_Remote("access_key_database", server, password)
  
  cloud.set("access_keys", access_keys, encryption_key=None)
except:
  raise Exception("EXCEPTON")

