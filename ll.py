from customtkinter import*

win = CTk()
win.geometry('400x400')
win.title("Task2")

text_box = CTkTextbox(win, width=180, height=280)
text_box.pack(pady=10)

text_entry = CTkEntry(win, width=380)
text_entry.pack(pady=10)

button = CTkButton(win, width=380, text="Клік")
button.pack()

win.mainloop()