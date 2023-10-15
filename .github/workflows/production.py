import os
import requests
import time
from upsonic import Upsonic_Remote
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
  cloud = Upsonic_Remote("access_key_database", server, password)
  
  if cloud.set("access_keys", access_keys, encryption_key=None) == None:
    raise Exception()
except:
  raise Exception("EXCEPTON")

