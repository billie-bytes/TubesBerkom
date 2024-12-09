import tkinter as tk

window = tk.Tk()
window.title("Relative Width and Height Example")
window.geometry("1920x1080")

# Create a label with relative width and height
label1 = tk.Label(window, text="This label resizes with the window 1", bg="lightblue")
label2 = tk.Label(window, text="This label resizes with the window 2", bg="lightblue")
label1.place(relx=0.7, rely=0.5, relwidth=0.3, relheight=0.3, anchor=tk.CENTER)
label2.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.3, anchor=tk.CENTER)
window.mainloop()