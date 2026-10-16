import tkinter as tk

from login import Login


if __name__ == "__main__":
    ventana = tk.Tk()
    app = Login(ventana)
    app.pack(fill=tk.BOTH, expand=True)
    ventana.mainloop()