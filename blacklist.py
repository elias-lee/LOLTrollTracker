# import tkinter as tk
# from tkinter import * 
# from PIL import Image, ImageTk
# from colorama import Fore, Back, Style

# root = tk.Tk()


# canvas = tk.Canvas(root, width=450, height=400) #spesifies the size of the gui
# canvas.place(anchor=CENTER)
# canvas.grid(columnspan=3) #initialize canvas with columns


# with open('lol_blacklist.txt') as f:
#     bl = f.readlines()
# bl_new = []
# for i in bl:
#   x = i.replace("\n","")
#   bl_new.append(x)

# #Entry

# #submit
# ids=tk.StringVar()
# entry1 = tk.Entry(root, textvariable = ids) 

# #def submit function
# emptystrings=[]

# def submit():     
#     names=ids.get()
#     x = names.replace(" joined the lobby", "")
#     x = x.split("\n")
#     emptyLabel.config(text="")
#     for player in x:
#           if player in bl_new:
#                 # print("the player "+ Fore.RED + player + Style.RESET_ALL+" is in blacklist")
#                 # bl_list.append(print("the player "+ Fore.RED + player + Style.RESET_ALL+" is in blacklist"))
#                 emptystrings.append("the player " + player +" is in blacklist \n")
#                 # emptyLabel.config(text= "the player " + player +" is in blacklist")
#                 # return f'the player {Fore.RED}{x}{Style.RESET_ALL} is in blacklist'
#           else:
#                 emptystrings.append("")
#     ids.set("")
#     emptyLabel.config(text= emptystrings[0]+emptystrings[1]+emptystrings[2]+emptystrings[3]+emptystrings[4], anchor=CENTER)
    

# #drawing
# #logo
# logo = Image.open('trollTracker.png')
# logo = logo.resize((450, 350))
# logo = ImageTk.PhotoImage(logo)
# logo_label=tk.Label(image = logo)
# logo_label.image = logo
# logo_label.grid(columns=3,row=0)
# #entry
# canvas.create_window(450, 400, window=entry1)
# entry1.grid(column=1,row=2)
# #button
# sub_btn=tk.Button(root,text = 'Check', command = submit)
# sub_btn.grid(column=1,row=3)
# sub_btn.config(anchor=CENTER)

# #result label
# emptyLabel = tk.Label(root, fg='red')
# emptyLabel.grid(column=1, row = 4)


# root.mainloop()



###-----------




import tkinter as tk
from tkinter import * 
from PIL import Image, ImageTk
from colorama import Fore, Back, Style

root = tk.Tk()


canvas = tk.Canvas(root) #spesifies the size of the gui
canvas.place(anchor=CENTER)
# canvas.pack(fill=X) #initialize canvas with columns


with open('lol_blacklist.txt') as f:
    bl = f.readlines()
bl_new = []
for i in bl:
  x = i.replace("\n","")
  bl_new.append(x)

#Entry

#submit
ids=tk.StringVar()
entry1 = tk.Entry(root, textvariable = ids) 

#def submit function
emptystrings=[]

def submit():     
    names=ids.get()
    x = names.replace(" joined the lobby", "")
    x = x.split("\n")
    try:
      emptyLabel.pack_forget()
      print("forgetting")
    except:
      pass
    emptyLabel = tk.Label(root, fg='red')
    emptyLabel.config(text="")
    for player in x:          
          if player in bl_new:
                # print("the player "+ Fore.RED + player + Style.RESET_ALL+" is in blacklist")
                # emptystrings.append("the player " + player +" is in blacklist \n")
                # return f'the player {Fore.RED}{x}{Style.RESET_ALL} is in blacklist'
                emptystrings = "the player " + player +" is in blacklist"
                emptyLabel = tk.Label(root, fg='red')
                emptyLabel.config(text=emptystrings)
                emptyLabel.pack()
          else:
                # emptystrings.append("")
                emptystrings =""
    ids.set("")
    # emptyLabel.config(text= emptystrings[0]+emptystrings[1]+emptystrings[2]+emptystrings[3]+emptystrings[4], anchor=CENTER)
    

#drawing
#logo
logo = Image.open('trollTracker.png')
logo = logo.resize((450, 350))
logo = ImageTk.PhotoImage(logo)
logo_label=tk.Label(image = logo)
logo_label.image = logo
logo_label.pack(fill=X)
#entry
canvas.create_window(450, 400, window=entry1)
entry1.pack(fill=X)
#button
sub_btn=tk.Button(root,text = 'Check', command = submit)
sub_btn.pack(fill=X)
sub_btn.config(anchor=CENTER)
#result label
# emptyLabel = tk.Label(root, fg='red')
# emptyLabel.config(text="")


root.mainloop()





# bl_new = []
# for i in bl:
#   x = i.replace("\n","")
#   bl_new.append(x)

# with open('player_list.txt') as f:
#     pl = f.readlines()




