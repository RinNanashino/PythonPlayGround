import tkinter as tk 
import sys 
import os 

#main window creation
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")

def on_ok_click():
    #Main Windows hideing
    root.withdraw()

    #create a new window
    new_window = tk.Toplevel(root)
    new_window.title("Choosen")
    new_window.geometry("300x200")

    #create a label and put on the new window
    label = tk.Label(new_window, text="You clicked OK!")
    #write the string to a file
    str0 = "You clicked OK!"
    path = '/home/moff/git_local_repository/PythonPlayGround/log.txt'
    f = open(path, 'w')
    f.write(str0)
    f.close()
    #insert 20pixels blank space
    label.pack(pady=20)

    #killed the application after 2 seconds
    new_window.after(2000,new_window.destroy)
    new_window.after(2000,sys.exit)

def on_cancel_click():
    #when cancel button clicked, just exit the application
    sys.exit()
    

#make the ok button put on the main window
ok_button = tk.Button(root,text="OK", command=on_ok_click)
ok_button.pack(pady=10)

#make the cancel button put on the main window
cancel_button = tk.Button(root,text="Cancel", command=on_cancel_click)
cancel_button.pack(pady=10)

#start the main event loop
root.mainloop()
