import tkinter as tk
import re
class Calculator:
    def __init__(self, master,result):
        self.master = master
        self.result = result
        
        master.title("Basic Python Calculator")
        #create screen
        self.screen = tk.Text(master,background='#141414',font=('Helvetica',32),height=1,state='disabled',
                foreground='white', bd=0, pady=50, padx=5,selectbackground='#141414',inactiveselectbackground='#141414')

        for x in range(1, 5):
            self.master.columnconfigure(x, weight=1)
            self.master.rowconfigure(x, weight=1)

        #put in master window
        self.screen.grid(row=0, column=0, columnspan=5, sticky=tk.W+tk.E+tk.N+tk.S)
        self.screen.configure(state="normal")

        #init screen value empty
        self.equation = ''

        #define size
        self.master.geometry('500x600')

        b1 =  self.createButton(7)
        b2 = self.createButton(8)
        b3 = self.createButton(9)
        b4 = self.createButton(u"\u00F7", bg='#212121')
        b5 = self.createButton(4)
        b6 = self.createButton(5)
        b7 = self.createButton(6)
        b8 = self.createButton(u"\u00D7", bg='#212121')
        b9 = self.createButton(1)
        b10 = self.createButton(2)
        b11 = self.createButton(3)
        b12 = self.createButton('-', bg='#212121')
        b13 = self.createButton(',')
        b14 = self.createButton(0)
        b15 = self.createButton(None)
        b16 = self.createButton('+', bg='#212121')
        b17 = self.createButton('DEL', None, bg='#212121')
        b18 = self.createButton('CE', None, bg='#212121')
        b19 = self.createButton('=', None, bg='#c41212')
        b15.config(state='disabled')
        buttons = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18,b19]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1,5):
            for column in range(4):
                buttons[count].grid(row=row,column=column, sticky=tk.W+tk.E+tk.N+tk.S)
                count += 1
        # arrange last button '=' at the bottom       
        buttons[16].grid(row=1, column=4, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S)
        buttons[17].grid(row=2, column=4, rowspan=2, sticky=tk.W+tk.E+tk.N+tk.S)
        buttons[18].grid(row=4, column=4, rowspan=1, sticky=tk.W+tk.E+tk.N+tk.S)

    def createButton(self,val,write=True,width=5,bg="black",fg="white"):
        return tk.Button(self.master, text=val, command = lambda:self.click(val,write,self.result), width=width,bg=bg,bd=0,fg=fg, font=('Helvetica',24))

    def click(self,text,write,result):
        if write == None:
            if text == '=' and self.equation:
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                self.equation = re.sub(u'\u00D7', '*', self.equation)
                self.equation = re.sub(r"((?<=^)|(?<=[^\.\d]))0+(\d+)", r"\1\2", self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
                self.result = True
            elif text == "CE":
                self.clear_screen()
            elif text == "DEL":
                self.del_screen()
        else:
            if result and type(text) == int:
                self.clear_screen()
                self.result = False
            if text == "+" or text == "-" or text == u"\u00D7" or text == u"\u00F7":
                self.result = False
            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state="normal")
        self.screen.delete('1.0', tk.END)
        self.screen.configure(state='disabled')


    def del_screen(self):
        self.equation = self.equation[:-1]
        self.screen.configure(state="normal")
        text = self.screen.get("1.0", tk.END)[:-2]
        self.screen.tag_config('val', justify=tk.RIGHT)
        self.screen.delete(1.0, tk.END)
        self.screen.insert(tk.END, text, 'val')
        self.screen.configure(state="disabled")


    def insert_screen(self, value, newline=False):
        self.screen.configure(state="normal")
        self.screen.tag_config('val',justify=tk.RIGHT)
        self.screen.insert(tk.END,str(value), 'val')
        self.equation += str(value)
        self.screen.configure(state="disabled")

root = tk.Tk()
my_gui = Calculator(root,False)
root.mainloop()
