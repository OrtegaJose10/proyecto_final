from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def fun_secion():
    global secion
    secion = Tk()
    secion.title("Ingresar al Sistema")
    secion.resizable(0,0)
    secion.geometry("770x470") #ancho, alto
    secion.configure()

    img_secion = Image.open("Imagenes/iniciar.png")

    resized = img_secion.resize((770,470))
    img_secion = ImageTk.PhotoImage(resized)

    label_imagen = Label(secion, image = img_secion)
    label_imagen.pack()
    label_imagen.place(x=0, y=0)

    img_net2 = Image.open("Imagenes/volver.png")

    resized = img_net2.resize((50,50))
    img_net2 = ImageTk.PhotoImage(resized)
    
    usuario_1=  StringVar()
    entry_usuario = Entry(secion, textvariable= usuario_1 , font=("Arial", 18),width=22,fg='white',bg='#000000', relief="flat")
    entry_usuario.pack
    entry_usuario.place(x=70, y=215)
    
    contraseña_1=  StringVar()
    entry_contraseña = Entry(secion, textvariable= contraseña_1 , font=("Arial", 18),width=22,fg='white',show="*",bg='#000000', relief="flat")
    entry_contraseña.pack
    entry_contraseña.place(x=70, y=296)

    def verificar_datos():
            usuario = usuario_1.get()
            if len(usuario) < 6:
                messagebox.showwarning("Usuario inválido", "debe ingresar el usuario con que se registro anterior mente")
            else:
                messagebox.showinfo("Usuario válido", "El usuario es válido.")
            contraseña = contraseña_1.get()
            if len(contraseña) < 8:
                messagebox.showwarning("Contraseña inválida", "Debe ingresar la contraseña con el que se registro anterior mente")
            else:
                messagebox.showinfo("Contraseña válida", "Sus datos son correctos,ya q sus datos estan verificados ")
                
    btn_verificar_contraseña= Button(secion, text= "      VERIFICAR      ", bg='#4E4FEB',font=("Arial", 14),width=19,cursor="hand2", relief="flat", command = verificar_datos)
    btn_verificar_contraseña.pack()
    btn_verificar_contraseña.place(x=155,y=380)

    btn_salir= Button(secion, text= "       SALIR       ", bg='#FFFFFF',font=("Arial", 15),width=20,cursor="hand2", relief="flat",command = secion.destroy)
    btn_salir.pack()
    btn_salir.place(x=420,y=380)
    
    btn_volver= Button(image=img_net2, bg='#000000',font=("Arial", 15),text="Salir",width=50,cursor="hand2", relief="flat",command = volver)
    btn_volver.pack()
    btn_volver.place(x=10,y=5)
    btn_volver= Button(secion, text="volver para iniciar secion", wraplength=100, fg='#FFFFFF' ,bg='#000000',font=("Arial", 13),height=2,width=11,cursor="hand2", relief="flat",command = volver)
    btn_volver.pack()
    btn_volver.place(x=60,y=5)

    mainloop()


def ir_l_m():
    secion.destroy()
    import Menu

def volver():
    secion.destroy()
    import inicio
    
def ir_l_f():
    secion.destroy()
    import formulario 

fun_secion()
