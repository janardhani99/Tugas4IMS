import pymysql

# Open database connection
db = pymysql.connect("localhost","root","","db_cloud9")

# prepare a cursor object using cursor() method
cursor = db.cursor()
#
# # execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")
#
# # Fetch a single row using fetchone() method.
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)

sql = """INSERT INTO tb_mahasiswa (nama, nim, umur, program_studi)
   VALUES ('Jena Janardhani', '1705551121', '19', 'Teknologi Informasi')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

