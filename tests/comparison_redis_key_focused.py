# Create a sql lite database that includes the following tables:
# 1. Customer (customer_id, first_name, last_name)
import time

import redis
from kot import KOT


number = 1000
find_number = 99999
edit_account_number = 10000
data_1 = "Ahmet"*5
data_2 = "Mehmet"*5



# REDIS
r = redis.Redis(host='localhost', port=6379, db=0)
time_1 = time.time()
big_list = {}
for x in range(0, number):
    r.set(str(x), str([data_1,data_2]))
time_2 = time.time()


# KOT
client_address_db = KOT("client_addressesa", enable_fast = True)
time_3 = time.time()
big_list = {}
for x in range(0, number):
    client_address_db.set(str(x), str([data_1,data_2]))
time_4 = time.time()




# REDIS
time_5 = time.time()
r.get(str(number-1))
time_6 = time.time()

# KOT
time_7 = time.time()
the_list = client_address_db.get(str(number-1))
time_8 = time.time()







print("WRITE")
print("REDIS:   ", time_2 - time_1)
print("KOT:     ", time_4 - time_3)

print("\nREAD")
print("REDIS:   ", time_6 - time_5)
print("KOT:     ", time_8 - time_7)



