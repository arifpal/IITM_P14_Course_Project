import tkinter as tk

root = tk.Tk()

var = tk.StringVar()

option1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1")
option1.pack()

option2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2")
option2.pack()

root.mainloop()



selected_option = var.get()
print(selected_option)
