import pymysql
conn=pymysql.connect(host="localhost", user="root", passwd="",  db="library")
kess= conn.cursor()
kess.execute("INSERT INTO `userr` (`studid`, `name1`, `name2`, `class`, `address`, `start`, `city`) VALUES (NULL, 'Sipho', 'Mgijima', 'Quantity Surveying', '3200 Nketa 11 Bulawayo', '2011-08-27', 'Bulawayo')")
conn.commit()
conn.close()

def geta():
    import pymysql
    conn=pymysql.connect(host="localhost", user="root", passwd="",  db="library")
    kess= conn.cursor()
    kess.execute("INSERT INTO `userr` (`studid`, `name1`, `name2`, `class`, `address`, `start`, `city`) VALUES (NULL, name1, name2, clas, addres, start, city)")
    conn.commit()
    kess.close()
  


