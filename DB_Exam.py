import MySQLdb

db = MySQLdb.connect("uws64-127.cafe24.com", "runa126", "Sunny20061216!", "runa126")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print("Database version : %s " % data)

db.close()
