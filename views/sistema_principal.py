import tkinter as tk


class SistemaPrincipal(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana, bg="#030708")
        self.ventana = ventana

        self.ventana.overrideredirect(False)
        self.ventana.geometry("900x600")
        self.ventana.title("Sistema principal")
        self.ventana.resizable(True, True)
        self.ventana.configure(bg="#030708")

        self.pack(fill=tk.BOTH, expand=True)

        tk.Label(
            self,
            text="Sistema principal",
            font=("Segoe UI", 24, "bold"),
            fg="#e5fbff",
            bg="#030708",
        ).pack(pady=(80, 12))

        tk.Label(
            self,
            text="Tu sistema está listo",
            font=("Segoe UI", 16),
            fg="#a0b0b5",
            bg="#030708",
        ).pack(pady=8)

        tk.Button(
            self,
            text="Salir",
            command=self.ventana.destroy,
            font=("Segoe UI", 11, "bold"),
            fg="#030708",
            bg="#36dce0",
            activebackground="#21b9bd",
            relief=tk.FLAT,
            cursor="hand2",
            padx=24,
            pady=8,
        ).pack(pady=32)