def main():
    import tkinter as tk
    import pymsql
    win = tk.Tk()
    win.title("Fun Library").geometry("400*400")

    title =  tk.Label(text="Enter new user details").grid()
    name1 = tk.Entry().grid()
    name2  = tk.Entry().grid()
    clas  = tk.Entry().grid()
    start = tk.Entry().grid()
    city  = tk.Entry().grid()
    addres  = tk.Entry().grid()
    button1 = tk.Button(text="Submit", bg="blue").grid()
    win.mainloop()

class new:
    def __init__(self, name1, name2, clas, start, city, addres, id=None):
        self.id=None
        self.name1=name1
        self.name2=name2
        self.clas=clas
        self.start=start
        self.city=city
        self.addres=addres

    def save(self):
        import pymysql
        conn=pymysql.connect(host="localhost", user="root", passwd="",  db="library")
        kess= conn.cursor()
        kess.execute("INSERT INTO `userr` (self.id=None, self.name1, self.name2, self.clas, self.addres, self.start, `city`) VALUES (NULL, 'Sipho', 'Mgijima', 'Quantity Surveying', '3200 Nketa 11 Bulawayo', '2011-08-27', 'Bulawayo')")
        conn.close()

newuser=new(None, 'Tawanda', 'Nyagwaya', 'Accounting', '34 King George, Avondale', '11-01-2004', 'Nyanga')
newuser.save()


if __name__ == "__main__":
    main()
