import tkinter as tk
from tkinterweb import HtmlFrame

root = tk.Tk()
root.title("내장 브라우저")

frame = HtmlFrame(root)
frame.pack(fill="both", expand=True)

frame.load_website("http://127.0.0.1:5000")

root.mainloop()
