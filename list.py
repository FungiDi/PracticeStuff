def geta():
    import pymsql
    conn=pymysql.connect(host="localhost", user="root", passwd="",  db="library")
    kess= conn.cursor()
    items = kess.execute("SELECT * FROM `userr` ")
    conn.close()
    print( items)

geta() 