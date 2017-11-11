import MySQLdb

db = MySQLdb.connect("localhost", "luke906", "lsw20061216!", "AIRBITCLUB")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()
