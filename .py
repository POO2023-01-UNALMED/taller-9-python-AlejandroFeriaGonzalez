import tkinter as tk
ventana = tk.Tk()
ventana.title("Eventos")
ventana.geometry("300x200")
def Ok(evento):
    print(evento)
    etiqueta.config(text="Click en botón OK")
def Cancelar(evento):
    etiqueta.config(text="Click en botón Cancelar")

button1 = tk.Button(ventana, text="OK")
button1.pack(side='top',anchor="w",padx=10,pady=10)
button1.bind("<Button>",lambda e: etiqueta.config(text="jeje"))
button2 = tk.Button(ventana, text="Cancelar")
button2.pack(side='left',anchor="n",padx=10,pady=10)
button2.bind("<Button>",Cancelar)
etiqueta = tk.Label(ventana, text="Presione un botón")
etiqueta.pack()
ventana.mainloop()
