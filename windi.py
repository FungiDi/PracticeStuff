import tkinter as tk
import pymysql
win = tk.Tk()
win.title("Fun Library")
win.geometry("400x400")

def save():
    import pymysql
    conn=pymysql.connect(host="localhost", user="root", passwd="",  db="library")
    kess= conn.cursor()
    #kess.execute("INSERT INTO `userr` (`studid`, `name1`, `name2`, `class`, `address`, `start`, `city`) VALUES (NULL, `%s`, `%s`, `%s`, `%s`, `%s`, `%s` )" %(str(name1.get()), str(name2.get()), str(clas.get()), str(addres.get()), str(start.get()), str(city.get())   ))
    kess.execute("""INSERT INTO `userr` (`name1`, `name2`, `class`, `address`, `start`, `city`) VALUES ( "%s", "%s", "%s", "%s", "%s", "%s" )""" %(str(name1.get()), str(name2.get()), str(clas.get()), str(addres.get()), str(start.get()), str(city.get())   ))
    conn.commit()
    conn.close()

    #import pymysql
    #conn=pymysql.connect(host="localhost", user="root", passwd="",  db="library")
    #kess= conn.cursor()
    #kess.execute("INSERT INTO `userr` (`studid`, `name1`, `name2`, `class`, `address`, `start`, `city`) VALUES (NULL, 'Sipho', 'Mgijima', 'Quantity Surveying', '3200 Nketa 11 Bulawayo', '2011-08-27', 'Bulawayo')")
    #conn.commit()
    #conn.close()


def nam():
    save()
    #print ([ str(name1.get()), str(name2.get()), str(clas.get()), str(start.get()),  str(city.get()), str(addres.get()) ] )
    



title =  tk.Label(text="Enter new user details").grid()
namea =  tk.Label(text="Name").grid(column=1, row=3,)
name1 = tk.Entry()
name1.grid(column=4, row= 3,)

nameb =  tk.Label(text="Surname").grid(column=1, row=5,)
name2  = tk.Entry()
name2.grid(column=4, row= 5,)

clasc =  tk.Label(text="Class").grid(column=1, row=7,)
clas  = tk.Entry()
clas.grid(column=4, row=7,)

startd =  tk.Label(text="Start Date").grid(column=1, row= 9)
start = tk.Entry()
start.grid(column=4, row= 9)

citye =  tk.Label(text="City").grid(column=1, row= 11)
city  = tk.Entry()
city.grid(column=4, row= 11)

addresf =  tk.Label(text="Address").grid(column=1, row=13)
addres  = tk.Entry()
addres.grid(column=4, row=13)

name = str(name1.get())
surname = str( name2.get())

button1 = tk.Button(text="Submit", bg="blue", command = nam).grid()

win.mainloop()


