from kot import KOT




db = KOT("access_key_database")

print(db.get("access_keys", no_cache=True))


db.set("access_keys", ["dsadsadsd"], cache_policy=10)