# Create a sql lite database that includes the following tables:
# 1. Customer (customer_id, first_name, last_name)
import time

import sqlite3
from kot import KOT


number = 100000
find_number = 99999
edit_account_number = 10000
data_1 = "Ahmet"*5
data_2 = "Mehmet"*5


#Cleaning
import os
if os.path.exists("mydb.db"):
    os.remove("mydb.db")
KOT.database_delete_all()



# SQLLITE
conn = sqlite3.connect('mydb.db')
cursor = conn.cursor()
time_1 = time.time()
cursor.execute('''CREATE TABLE IF NOT EXISTS
                    Customer(customer_id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT)''')
for x in range(0, number):
    cursor.execute("INSERT INTO Customer VALUES (?, ?, ?)", (str(x),data_1, data_2))
conn.commit()
time_2 = time.time()


# KOT
client_address_db = KOT("client_addresses")
time_3 = time.time()
big_list = {}
for x in range(0, number):
    big_list[str(x)] = [data_1,data_2]
client_address_db.set("users", big_list)
time_4 = time.time()




# SQLLITE
time_5 = time.time()
cursor.execute(f"SELECT * FROM Customer WHERE customer_id = {find_number}")
print(cursor.fetchone())
time_6 = time.time()

# KOT
the_list = client_address_db.get("users")
time_7 = time.time()
print(the_list[str(find_number)])
time_8 = time.time()



# SQLLITE
time_9 = time.time()
for x in range(0, edit_account_number):
    cursor.execute(f"UPDATE Customer SET first_name = '{data_2}', last_name = '{data_2}' WHERE customer_id = {x}")
conn.commit()
time_10 = time.time()

# KOT
time_11 = time.time()
for x in range(0, edit_account_number):
    the_list[str(x)] = [data_2,data_2]
client_address_db.set("users", the_list)
time_12 = time.time()


# Get all datas
# SQLLITE
time_13 = time.time()
cursor.execute(f"SELECT * FROM Customer")
cursor.fetchall()
time_14 = time.time()

# KOT
time_15 = time.time()
client_address_db.get("users")
time_16 = time.time()







print("WRITE")
print("SQLLITE: ", time_2 - time_1)
print("KOT:     ", time_4 - time_3)

print("\nREAD")
print("SQLLITE: ", time_6 - time_5)
print("KOT:     ", time_8 - time_7)

print("\nUPDATE")
print("SQLLITE: ", time_10 - time_9)
print("KOT:     ", time_12 - time_11)

print("\nREAD ALL")
print("SQLLITE: ", time_14 - time_13)
print("KOT:     ", time_16 - time_15)

print("\nSIZE")
print("SQLLITE: ", os.path.getsize("mydb.db"))
print("KOT:     ", client_address_db.size_all())