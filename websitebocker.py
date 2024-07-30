from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry('650x400')
window.minsize(650, 400)
window.maxsize(650, 400)
window.title("Website Blocker")

Heading = Label(window, text='Website Blocker', font='arial')
Heading.pack()

host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'
ip_address = '127.0.0.1'

Label1 = Label(window, text='Enter Website:', font='arial 13 bold')
Label1.place(x=5, y=60)
enter_website = Text(window, font='arial', height=2, width=40)
enter_website.place(x=140, y=60)

def Blocker():
    print('****************BLOCKER START****************')
    website_lists = enter_website.get(1.0, END).strip()
    websites = list(website_lists.split(","))
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for web in websites:
            web = web.strip()
            if web in file_content:
                messagebox.showinfo("Information", "Already Blocked " + web)
                print('Already Blocked ' + web)
            else:
                host_file.write(ip_address + " " + web + '\n')
                messagebox.showinfo("Information", "Blocked " + web)
                print('Blocked ' + web)
    with open(host_path, 'r') as host_file:
        after_file_write = host_file.read()
        print('------------AFTER FILE WRITE------------')
        print('------------FILE START------------')
        print(after_file_write)
        print('------------FILE END------------')
    print('****************BLOCKER END****************')

def Unblock():
    print('****************UNBLOCKER START****************')
    website_lists = enter_website.get(1.0, END).strip()
    websites = list(website_lists.split(","))
    with open(host_path, 'r') as host_file:
        file_content = host_file.readlines()
    with open(host_path, 'w') as host_file:
        for line in file_content:
            if not any(web.strip() in line for web in websites):
                host_file.write(line)
    messagebox.showwarning("Information", "Unblocked " + ', '.join(web.strip() for web in websites))
    with open(host_path, 'r') as host_file:
        after_file_write = host_file.read()
        print('------------AFTER FILE WRITE------------')
        print('------------FILE START------------')
        print(after_file_write)
        print('------------FILE END------------')
    print('****************UNBLOCKER END****************')

block_button = Button(window, text='Block', font='arial', pady=5, command=Blocker, width=6, bg='royal blue1', activebackground='grey')
block_button.place(x=230, y=150)
unblock_button = Button(window, text='UnBlock', font='arial', pady=5, command=Unblock, width=6, bg='royal blue1', activebackground='grey')
unblock_button.place(x=350, y=150)
window.mainloop()
