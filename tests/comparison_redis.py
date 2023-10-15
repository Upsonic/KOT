# Create a sql lite database that includes the following tables:
# 1. Customer (customer_id, first_name, last_name)
import time

import redis
from upsonic import Upsonic


number = 100
find_number = 99999
edit_account_number = 10000
data_1 = "Ahmet"*5
data_2 = "Mehmet"*5




# REDIS
r = redis.Redis(host='localhost', port=6379, db=0)
time_1 = time.time()
big_list = {}
for x in range(0, number):
    big_list[str(x)] = [data_1,data_2]
r.set("users", str(big_list))
time_2 = time.time()


# Upsonic
client_address_db = Upsonic("client_addressesa", enable_fast = True)
time_3 = time.time()
big_list = {}
for x in range(0, number):
    big_list[str(x)] = [data_1,data_2]
client_address_db.set("users", big_list)
time_4 = time.time()




# REDIS
time_5 = time.time()
r.get("users")
time_6 = time.time()

# Upsonic
time_7 = time.time()
the_list = client_address_db.get("users")
time_8 = time.time()



# REDIS
time_9 = time.time()
for x in range(0, edit_account_number):
    the_list[str(x)] = [data_2,data_2]
r.set("users", str(the_list))
time_10 = time.time()

# Upsonic
time_11 = time.time()
for x in range(0, edit_account_number):
    the_list[str(x)] = [data_2,data_2]
client_address_db.set("users", the_list)
time_12 = time.time()










print("WRITE")
print("REDIS:   ", time_2 - time_1)
print("Upsonic:     ", time_4 - time_3)

print("\nREAD")
print("REDIS:   ", time_6 - time_5)
print("Upsonic:     ", time_8 - time_7)

print("\nUPDATE")
print("REDIS:   ", time_10 - time_9)
print("Upsonic:     ", time_12 - time_11)



