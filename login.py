from pathlib import Path
import tkinter as tk
from tkinter import messagebox

from views.sistema_principal import SistemaPrincipal

# Paleta de colores optimizada (Cyberpunk)
COLOR_FONDO = "#030708"  
COLOR_BARRA = "#030708"
COLOR_CAMPO = "#092321"
COLOR_TEXTO = "#e5fbff"
COLOR_ETIQUETA = "#8a9a9f"  
COLOR_BORDE = "#3ad5dc"
COLOR_CERRAR = "#ff5261"

# Proporciones estilizadas y verticales
ANCHO_VENTANA = 420     
ALTO_VENTANA = 620
ANCHO_CONTENIDO = 320   
MARGEN_IZQUIERDO = 50   


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
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.title("Sistema Login")
        self.ventana.config(bg=COLOR_FONDO)
        self.ventana.resizable(False, False)
        self.ventana.overrideredirect(True)

        # Eventos para arrastrar la ventana sin bordes
        self.ventana.bind("<Button-1>", self._iniciar_movimiento)
        self.ventana.bind("<B1-Motion>", self._mover_ventana)

    def _iniciar_movimiento(self, evento):
        self.x = evento.x
        self.y = evento.y

    def _mover_ventana(self, evento):
        deltax = evento.x - self.x
        deltay = evento.y - self.y
        x = self.ventana.winfo_x() + deltax
        y = self.ventana.winfo_y() + deltay
        self.ventana.geometry(f"+{x}+{y}")

    def _cargar_imagenes(self):
        carpeta_iconos = self.ruta_proyecto / "iconos"
        carpeta_imagenes = self.ruta_proyecto / "imagnes"  

        try:
            self.icono_img = tk.PhotoImage(file=str(carpeta_iconos / "icono.png"))
            self.logo_img = tk.PhotoImage(file=str(carpeta_imagenes / "logo.png"))
            self.ventana.iconphoto(True, self.icono_img)
            self.icono_barra_img = self.icono_img.subsample(5, 5)
            self.logo_img_reducido = self.logo_img.zoom(2, 2).subsample(5, 5)
        except Exception:
            self.icono_barra_img = None
            self.logo_img_reducido = None

    def _crear_barra_superior(self):
        barra = tk.Frame(self, bg=COLOR_BARRA, height=50)
        barra.pack(fill=tk.X)
        barra.pack_propagate(False)

        if self.icono_barra_img:
            tk.Label(barra, image=self.icono_barra_img, bg=COLOR_BARRA, borderwidth=0).pack(side=tk.LEFT, padx=(15, 8))

        tk.Label(
            barra,
            text="Sistema Login",
            font=("Segoe UI", 13, "bold"),
            fg="#a0b0b5",
            bg=COLOR_BARRA,
        ).pack(side=tk.LEFT, pady=12)

        # Botón Salir en la esquina superior derecha
        boton_salir = tk.Canvas(barra, width=40, height=40, bg=COLOR_BARRA, highlightthickness=0, cursor="hand2")
        boton_salir.pack(side=tk.RIGHT, padx=15, pady=5)
        boton_salir.create_oval(2, 2, 38, 38, fill="#1a1213", outline="#401116", width=1)
        boton_salir.create_line(12, 12, 12, 28, 24, 31, 24, 9, 12, 12, fill=COLOR_CERRAR, width=2)
        boton_salir.create_line(18, 20, 30, 20, fill=COLOR_CERRAR, width=2)
        boton_salir.create_line(26, 16, 30, 20, 26, 24, fill=COLOR_CERRAR, width=2)
        boton_salir.bind("<Button-1>", lambda evento: self.ventana.destroy())

    def _puntos_rectangulo_redondeado(self, x1, y1, x2, y2, radio):
        return [
            x1 + radio, y1, x2 - radio, y1, x2, y1, x2, y1 + radio,
            x2, y2 - radio, x2, y2, x2 - radio, y2, x1 + radio, y2,
            x1, y2, x1, y2 - radio, x1, y1 + radio, x1, y1
        ]

    def _crear_contenido(self):
        if self.logo_img_reducido:
            tk.Label(self, image=self.logo_img_reducido, bg=COLOR_FONDO, borderwidth=0).place(relx=0.5, y=130, anchor="center")
        else:
            circuito_placeholder = tk.Canvas(self, width=120, height=120, bg="#051214", highlightthickness=1, highlightbackground="#15585a")
            circuito_placeholder.place(relx=0.5, y=130, anchor="center")
            circuito_placeholder.create_text(60, 60, text="[ CIRCUITO ]", fill="#3ad5dc", font=("Arial", 10))

        tk.Label(
            self,
            text="Iniciar sesión",
            font=("Segoe UI", 24, "bold"),
            fg="#ffffff",
            bg=COLOR_FONDO,
        ).place(relx=0.5, y=230, anchor="center")

        self.campo_usuario = self._crear_campo("Usuario", y=280)
        self.campo_contrasena = self._crear_campo("Contraseña", y=365, ocultar=True)
        
        self.campo_usuario.bind("<Return>", self._ingresar_con_enter)
        self.campo_contrasena.bind("<Return>", self._ingresar_con_enter)

        self.boton_ingresar = tk.Canvas(
            self,
            width=ANCHO_CONTENIDO,
            height=50,
            bg=COLOR_FONDO,
            highlightthickness=0,
            cursor="hand2",
        )
        self.boton_ingresar.place(x=MARGEN_IZQUIERDO, y=470)
        self.boton_ingresar.create_polygon(
            self._puntos_rectangulo_redondeado(2, 2, ANCHO_CONTENIDO - 2, 48, 24),
            smooth=True,
            splinesteps=32,
            fill="#21b9bd",
            outline=COLOR_BORDE,
            width=1,
        )
        self.boton_ingresar.create_text(
            ANCHO_CONTENIDO // 2,
            25,
            text="Ingresar",
            font=("Segoe UI", 14, "bold"),
            fill="#030708",
        )
        self.boton_ingresar.bind("<Button-1>", lambda evento: self._ingresar())
        self.boton_ingresar.bind("<Enter>", lambda evento: self.boton_ingresar.itemconfig(1, fill="#36dce0"))
        self.boton_ingresar.bind("<Leave>", lambda evento: self.boton_ingresar.itemconfig(1, fill="#21b9bd"))
        
        self.campo_usuario.focus_set()

    def _crear_campo(self, texto, y, ocultar=False):
        tk.Label(
            self,
            text=texto,
            font=("Segoe UI", 10),
            fg=COLOR_ETIQUETA,
            bg=COLOR_FONDO,
        ).place(x=MARGEN_IZQUIERDO + 5, y=y)

        lienzo = tk.Canvas(
            self,
            width=ANCHO_CONTENIDO,
            height=44,
            bg=COLOR_FONDO,
            highlightthickness=0,
        )
        lienzo.place(x=MARGEN_IZQUIERDO, y=y + 22)
        
        lienzo.create_polygon(
            self._puntos_rectangulo_redondeado(2, 2, ANCHO_CONTENIDO - 2, 42, 21),
            smooth=True,
            splinesteps=32,
            fill=COLOR_CAMPO,
            outline="#123537",
            width=1,
        )

        opciones = {
            "font": ("Segoe UI", 11),
            "fg": COLOR_TEXTO,
            "bg": COLOR_CAMPO,
            "insertbackground": COLOR_TEXTO,
            "relief": tk.FLAT,
            "borderwidth": 0,
        }
        if ocultar:
            opciones["show"] = "*"

        campo = tk.Entry(lienzo, **opciones)
        lienzo.create_window(
            ANCHO_CONTENIDO // 2,
            22,
            window=campo,
            width=ANCHO_CONTENIDO - 35
        )
        return campo

    def _ingresar_con_enter(self, evento):
        self._ingresar()

    def _ingresar(self):
        ventana = self.ventana
        self.destroy()
        SistemaPrincipal(ventana)
