def main():
    import tkinter as tk
    import pymysql
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
if __name__ == "__main__":
    main()




