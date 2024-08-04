import hupper
import tkinter as tk
from tkinter import StringVar
import time

def start_reloader():
    reloader = hupper.start_reloader('app.main')
    time.sleep(10)





def main():
    def on_focus_in(event,):
        if entry.get() == placeholder_text:
            entry.delete(0, tk.END)
            entry.config(fg='black')

    def on_focus_out(event,):
        if entry.get() == '':
            entry.insert(0, placeholder_text)
            entry.config(fg='grey')

    root = tk.Tk()
    root.geometry('680x750+1900+0')

# --------------------------------------------------------------------------------------------------------------------------------
    instance_label = tk.Label(root,text = "Instance: (default = sphere)",justify="left")
    instance_label.grid(row=0,column=0)
    instance_entry_def_text = StringVar()
    instance_entry = tk.Entry(
        root,
        width =30,
        textvariable = instance_entry_def_text,
        justify="left",
           
            )

    instance_entry.grid(row=1,column=0,padx = 20, pady =0 )
    instance_entry_def_text.set("sphere")
# -------------------------------------------------------------------------------------------------------------------------------
    stagedb_label = tk.Label(root,text = "Staging Database:")
    stagedb_label.grid(row=2,column=0)

    stagedb_entry = tk.Entry(root,width = 30)
    stagedb_entry.grid(row=3,column=0)
# -------------------------------------------------------------------------------------------------------------------------------- 
    placeholder_text = "###MMDDYY"
    prefix_label = tk.Label(root,text = "Prefix:")
    prefix_label.grid(row=4,column=0)
    prefix_entry = tk.Entry(root,width = 30,fg="grey")
    prefix_entry.grid(row=5,column=0)
    prefix_entry.insert(0,placeholder_text)
    prefix_entry.bind("<FocusOut>", on_focus_out)
    prefix_entry.bind("<FocusIn>", on_focus_in)

# -------------------------------------------------------------------------------------------------------------------------------- 
    root.mainloop()
    
if __name__ == "__main__":
    start_reloader()
    main()