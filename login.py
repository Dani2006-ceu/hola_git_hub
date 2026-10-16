from pathlib import Path
import tkinter as tk


COLOR_FONDO = "#000000"
COLOR_BARRA = "#111111"
COLOR_CAMPO = "#151515"
COLOR_TEXTO = "#f3f6ff"
COLOR_ETIQUETA = "#d0d0d0"
COLOR_RESALTADO = "#29c9d2"
COLOR_CERRAR = "#e05d6f"


class Login(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana, bg=COLOR_FONDO)
        self.ventana = ventana
        self.ruta_proyecto = Path(__file__).resolve().parent

        self._configurar_ventana()
        self._cargar_imagenes()
        self._crear_barra_superior()
        self._crear_contenido()

    def _configurar_ventana(self):
        self.ventana.geometry("400x530")
        self.ventana.title("Sistema Login")
        self.ventana.config(bg=COLOR_FONDO)
        self.ventana.resizable(False, False)
        self.ventana.overrideredirect(True)

    def _cargar_imagenes(self):
        carpeta_iconos = self.ruta_proyecto / "iconos"
        carpeta_imagenes = self.ruta_proyecto / "imagnes"

        self.icono_img = tk.PhotoImage(file=str(carpeta_iconos / "icono.png"))
        self.logo_img = tk.PhotoImage(file=str(carpeta_imagenes / "logo.png"))
        self.ventana.iconphoto(True, self.icono_img)

    def _crear_barra_superior(self):
        barra = tk.Frame(self, bg=COLOR_BARRA, height=40)
        barra.pack(fill=tk.X)
        barra.pack_propagate(False)

        self.icono_barra_img = self.icono_img.subsample(5, 5)
        tk.Label(
            barra,
            image=self.icono_barra_img,
            bg=COLOR_BARRA,
            borderwidth=0,
        ).pack(side=tk.LEFT, padx=(10, 8), pady=6)

        tk.Label(
            barra,
            text="Sistema Login",
            font=("Segoe UI", 10, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_BARRA,
        ).pack(side=tk.LEFT)

        tk.Button(
            barra,
            text="×",
            width=4,
            command=self.ventana.destroy,
            bg=COLOR_BARRA,
            fg=COLOR_TEXTO,
            activebackground=COLOR_CERRAR,
            activeforeground="#ffffff",
            relief=tk.FLAT,
            borderwidth=0,
            cursor="hand2",
        ).pack(side=tk.RIGHT, fill=tk.Y)

    def _crear_contenido(self):
        self.logo_img_reducido = self.logo_img.subsample(4, 4)
        tk.Label(
            self,
            image=self.logo_img_reducido,
            bg=COLOR_FONDO,
            borderwidth=0,
        ).place(relx=0.5, y=132, anchor="center")

        tk.Label(
            self,
            text="Iniciar sesión",
            font=("Segoe UI", 20, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_FONDO,
        ).place(relx=0.5, y=225, anchor="center")

        self.campo_usuario = self._crear_campo("Usuario", y=270)
        self.campo_contrasena = self._crear_campo(
            "Contraseña",
            y=355,
            ocultar=True,
        )
        self.campo_usuario.focus_set()

    def _crear_campo(self, texto, y, ocultar=False):
        tk.Label(
            self,
            text=texto,
            font=("Segoe UI", 10),
            fg=COLOR_ETIQUETA,
            bg=COLOR_FONDO,
        ).place(x=55, y=y)

        opciones = {
            "font": ("Segoe UI", 11),
            "fg": COLOR_TEXTO,
            "bg": COLOR_CAMPO,
            "insertbackground": "#ffffff",
            "relief": tk.FLAT,
            "highlightthickness": 1,
            "highlightbackground": "#353535",
            "highlightcolor": COLOR_RESALTADO,
        }
        if ocultar:
            opciones["show"] = "*"

        campo = tk.Entry(self, **opciones)
        campo.place(x=55, y=y + 25, width=290, height=36)
        return campo
