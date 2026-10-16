from pathlib import Path
import tkinter as tk
from tkinter import messagebox

COLOR_FONDO = "#000000"
COLOR_BARRA = "#000000"
COLOR_CAMPO = "#092321"
COLOR_TEXTO = "#e5fbff"
COLOR_ETIQUETA = "#b9eaf0"
COLOR_RESALTADO = "#36dce0"
COLOR_BORDE = "#3ad5dc"
COLOR_CERRAR = "#ff5261"
ANCHO_VENTANA = 550
ALTO_VENTANA = 650
ANCHO_CONTENIDO = 430
MARGEN_IZQUIERDO = 68


class Login(tk.Frame):
    def __init__(self, ventana):
        super().__init__(ventana, bg=COLOR_FONDO)
        self.pack(fill=tk.BOTH, expand=True) # Empaquetar el frame principal
        self.ventana = ventana
        self.ruta_proyecto = Path(__file__).resolve().parent

        self._configurar_ventana()
        self._cargar_imagenes()
        self._crear_barra_superior()
        self._crear_fondo_decorativo()
        self._crear_contenido()

    def _configurar_ventana(self):
        self.ventana.geometry(f"{ANCHO_VENTANA}x{ALTO_VENTANA}")
        self.ventana.title("Sistema Login")
        self.ventana.config(bg=COLOR_FONDO)
        self.ventana.resizable(False, False)
        self.ventana.overrideredirect(True)

    def _cargar_imagenes(self):
        carpeta_iconos = self.ruta_proyecto / "iconos"
        carpeta_imagenes = self.ruta_proyecto / "imagnes"

        # Intenta cargar imágenes si existen, si no, usa fallbacks para pruebas
        try:
            self.icono_img = tk.PhotoImage(file=str(carpeta_iconos / "icono.png"))
            self.logo_img = tk.PhotoImage(file=str(carpeta_imagenes / "logo.png"))
            self.ventana.iconphoto(True, self.icono_img)
            self.icono_barra_img = self.icono_img.subsample(5, 5)
            self.logo_img_reducido = self.logo_img.zoom(2, 2).subsample(5, 5)
        except Exception:
            # Fallbacks vacíos si no encuentra los archivos físicos aún
            self.icono_barra_img = None
            self.logo_img_reducido = None

    def _crear_barra_superior(self):
        # Aumentamos ligeramente el alto a 52 para que el botón de salir quepa perfectamente arriba
        barra = tk.Frame(self, bg=COLOR_BARRA, height=52)
        barra.pack(fill=tk.X)
        barra.pack_propagate(False)

        if self.icono_barra_img:
            tk.Label(
                barra,
                image=self.icono_barra_img,
                bg=COLOR_BARRA,
                borderwidth=0,
            ).pack(side=tk.LEFT, padx=(12, 8), pady=1)

        tk.Label(
            barra,
            text="Sistema Login",
            font=("Segoe UI", 16, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_BARRA,
        ).pack(side=tk.LEFT, pady=10)

        # --- SE MOVIÓ EL BOTÓN SALIR AQUÍ (ARRIBA A LA DERECHA) ---
        boton_salir = tk.Canvas(
            barra,
            width=50,
            height=50,
            bg=COLOR_BARRA,
            highlightthickness=0,
            cursor="hand2",
        )
        boton_salir.pack(side=tk.RIGHT, padx=12, pady=1)

        # Círculo externo del botón miniatura superior
        boton_salir.create_oval(4, 4, 46, 46, fill="#18090b", outline="#401116", width=2)
        # Símbolo estilizado de puerta/salida en el botón pequeño
        boton_salir.create_line(16, 14, 16, 36, 30, 40, 30, 10, 16, 14, fill=COLOR_CERRAR, width=2)
        boton_salir.create_line(22, 25, 38, 25, fill=COLOR_CERRAR, width=2)
        boton_salir.create_line(34, 20, 38, 25, 34, 30, fill=COLOR_CERRAR, width=2)
        
        boton_salir.bind("<Button-1>", lambda evento: self.ventana.destroy())

    def _crear_fondo_decorativo(self):
        fondo = tk.Canvas(
            self,
            width=ANCHO_VENTANA,
            height=ALTO_VENTANA - 52,
            bg=COLOR_FONDO,
            highlightthickness=0,
        )
        fondo.place(x=0, y=52)

        for margen, color in (
            (0, "#03110f"),
            (14, "#041512"),
            (28, "#061916"),
            (42, "#081b18"),
        ):
            fondo.create_oval(
                -110 + margen,
                550 + margen,
                415 - margen,
                770 - margen,
                fill=color,
                outline="",
            )

        # Removido el óvalo rojo intermedio que envolvía al viejo botón "feo"

    def _puntos_rectangulo_redondeado(self, x1, y1, x2, y2, radio):
        # Genera la lista de puntos necesaria para crear un polígono con esquinas curvas
        return [
            x1 + radio, y1,
            x2 - radio, y1,
            x2, y1,
            x2, y1 + radio,
            x2, y2 - radio,
            x2, y2,
            x2 - radio, y2,
            x1 + radio, y2,
            x1, y2,
            x1, y2 - radio,
            x1, y1 + radio,
            x1, y1
        ]

    def _crear_contenido(self):
        if self.logo_img_reducido:
            tk.Label(
                self,
                image=self.logo_img_reducido,
                bg=COLOR_FONDO,
                borderwidth=0,
            ).place(relx=0.5, y=182, anchor="center")

        tk.Label(
            self,
            text="Iniciar sesión",
            font=("Segoe UI", 28, "bold"),
            fg=COLOR_TEXTO,
            bg=COLOR_FONDO,
        ).place(relx=0.5, y=325, anchor="center")

        self.campo_usuario = self._crear_campo("Usuario", y=398)
        self.campo_contrasena = self._crear_campo(
            "Contraseña",
            y=483,
            ocultar=True,
        )
        self.campo_usuario.bind("<Return>", self._ingresar_con_enter)
        self.campo_contrasena.bind("<Return>", self._ingresar_con_enter)

        self.boton_ingresar = tk.Canvas(
            self,
            width=ANCHO_CONTENIDO,
            height=62,
            bg=COLOR_FONDO,
            highlightthickness=0,
            cursor="hand2",
        )
        self.boton_ingresar.place(x=MARGEN_IZQUIERDO, y=575)
        self.boton_ingresar.create_polygon(
            self._puntos_rectangulo_redondeado(
                2, 2, ANCHO_CONTENIDO - 2, 60, 16
            ),
            smooth=True,
            splinesteps=24,
            fill="#21b9bd",
            outline=COLOR_BORDE,
            width=2,
        )
        self.boton_ingresar.create_text(
            ANCHO_CONTENIDO // 2,
            31,
            text="Ingresar",
            font=("Segoe UI", 18, "bold"),
            fill="#062226",
        )
        self.boton_ingresar.bind("<Button-1>", lambda evento: self._ingresar())
        self.boton_ingresar.bind(
            "<Enter>",
            lambda evento: self.boton_ingresar.itemconfig(1, fill="#36dce0"),
        )
        self.boton_ingresar.bind(
            "<Leave>",
            lambda evento: self.boton_ingresar.itemconfig(1, fill="#21b9bd"),
        )
        self._crear_pie()
        self.campo_usuario.focus_set()

    def _crear_pie(self):
        tk.Label(
            self,
            text="FECHA",
            font=("Segoe UI", 8),
            fg="#657272",
            bg=COLOR_FONDO,
        ).place(x=8, y=626)

        tk.Label(
            self,
            text="FIRMA",
            font=("Segoe UI", 8),
            fg="#657272",
            bg=COLOR_FONDO,
        ).place(x=540, y=612, anchor="ne")
        tk.Label(
            self,
            text="Alex Moran",
            font=("Segoe UI", 8),
            fg=COLOR_ETIQUETA,
            bg=COLOR_FONDO,
        ).place(x=540, y=632, anchor="ne")

    def _crear_campo(self, texto, y, ocultar=False):
        tk.Label(
            self,
            text=texto,
            font=("Segoe UI", 10),
            fg=COLOR_ETIQUETA,
            bg=COLOR_FONDO,
        ).place(x=MARGEN_IZQUIERDO + 4, y=y)

        lienzo = tk.Canvas(
            self,
            width=ANCHO_CONTENIDO,
            height=52,
            bg=COLOR_FONDO,
            highlightthickness=0,
        )
        lienzo.place(x=MARGEN_IZQUIERDO, y=y + 25)
        puntos = self._puntos_rectangulo_redondeado(
            1, 1, ANCHO_CONTENIDO - 1, 51, 14
        )
        lienzo.create_polygon(
            self._puntos_rectangulo_redondeado(
                2, 2, ANCHO_CONTENIDO - 2, 50, 13
            ),
            smooth=True,
            splinesteps=24,
            fill=COLOR_CAMPO,
            outline="#15585a",
            width=5,
        )
        lienzo.create_polygon(
            puntos,
            smooth=True,
            splinesteps=24,
            fill=COLOR_CAMPO,
            outline=COLOR_BORDE,
            width=2,
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

        # --- COMPLETADO DE LA LÍNEA CORTADA ---
        campo = tk.Entry(lienzo, **opciones)
        # Posiciona la caja de texto dentro del Canvas decorativo redondeado
        lienzo.create_window(
            ANCHO_CONTENIDO // 2,
            26,
            window=campo,
            width=ANCHO_CONTENIDO - 30  # Le damos margen interno para que no choque el texto con la curva
        )
        return campo

    def _ingresar_con_enter(self, evento):
        self._ingresar()

    def _ingresar(self):
        usuario = self.campo_usuario.get()
        contra = self.campo_contrasena.get()
        if usuario and contra:
            messagebox.showinfo("Login", f"¡Bienvenido, {usuario}!")
        else:
            messagebox.showwarning("Login", "Por favor completa todos los campos.")


# Bloque de ejecución para probar tu clase directamente
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = Login(ventana_principal)
    ventana_principal.mainloop()
