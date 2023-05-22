from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def fun_login():
    global login 
    login = Tk()
    login.title("Ingresar al Sistema")
    login.resizable(0,0)
    login.geometry("770x470") #ancho, alto
    login.configure()

    img_login = Image.open("Imagenes/crear_usuario.png")

    resized = img_login.resize((770,470))
    img_login = ImageTk.PhotoImage(resized)

    label_imagen = Label(login, image = img_login)
    label_imagen.pack()
    label_imagen.place(x=0, y=0)

    img_net2 = Image.open("Imagenes/volver.png")

    resized = img_net2.resize((50,50))
    img_net2 = ImageTk.PhotoImage(resized)

    label_imagen = Label(login, image = img_net2, bg='black')
    label_imagen.pack()
    label_imagen.place(x=2, y=5)
    
    nombre_1=  StringVar()
    entry_nombre = Entry(login, textvariable= nombre_1, font=("Arial", 15),width=20,fg='white',bg='black', relief="flat")
    entry_nombre.pack
    entry_nombre.place(x=118, y=167) 

    gmail_1=  StringVar()
    entry_gmail = Entry(login, textvariable= gmail_1, font=("Arial", 15),width=20,fg='white',bg='black', relief="flat")
    entry_gmail.pack
    entry_gmail.place(x=118, y=227)

    usuario_1=  StringVar()
    entry_usuario = Entry(login, textvariable= usuario_1 , font=("Arial", 15),width=20,fg='white',bg='black', relief="flat")
    entry_usuario.pack
    entry_usuario.place(x=118, y=280)
    
    contraseña_1=  StringVar()
    entry_contraseña = Entry(login, textvariable= contraseña_1 , font=("Arial", 15),width=20,fg='white',show="*",bg='black', relief="flat")
    entry_contraseña.pack
    entry_contraseña.place(x=118, y=335)

    def verificar_datos():
            nombre = nombre_1.get()
            if len(nombre) == 0:
                messagebox.showwarning("Nombre inválido", "El campo de nombre está vacío.")
            elif not nombre.isalpha():
                messagebox.showwarning("Nombre inválido", "El campo de nombre debe contener solo letras.")
            else:
                messagebox.showinfo("Nombre válido", "El nombre es válido.")
            email = gmail_1.get()
            if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                messagebox.showwarning("Correo electrónico inválido", "Ingrese una dirección de correo electrónico válida.")
            else:
                messagebox.showinfo("Datos válidos", "Sus datos son correctos, puede volver para iniciar sesión.")
            usuario = usuario_1.get()
            if len(usuario) < 6:
                messagebox.showwarning("Usuario inválido", "El usuario debe tener al menos 6 caracteres.")
            elif not usuario.isalnum():
                messagebox.showwarning("Usuario inválido", "El usuario debe contener sólo caracteres alfanuméricos.")
            else:
                messagebox.showinfo("Usuario válido", "El usuario es válido.")
            contraseña = contraseña_1.get()
            if len(contraseña) < 8:
                messagebox.showwarning("Contraseña inválida", "La contraseña debe tener al menos 8 caracteres.")
            elif not any(char.isdigit() for char in contraseña):
                messagebox.showwarning("Contraseña inválida", "La contraseña debe contener al menos un número.")
            elif not any(char.isupper() for char in contraseña):
                messagebox.showwarning("Contraseña inválida", "La contraseña debe contener al menos una letra mayúscula.")
            elif not any(char.islower() for char in contraseña):
                messagebox.showwarning("Contraseña inválida", "La contraseña debe contener al menos una letra minúscula.")
            else:
                messagebox.showinfo("Contraseña válida", "Sus datos son correctos,porfavor precione volver para iniciar sesion")
                
    btn_verificar_contraseña= Button(login, text= "      VERIFICAR      ", bg='#4E4FEB',font=("Arial", 14),width=19,cursor="hand2", relief="flat", command = verificar_datos)
    btn_verificar_contraseña.pack()
    btn_verificar_contraseña.place(x=120,y=385)

    btn_salir= Button(login, text= "       SALIR       ", bg='#FFFFFF',font=("Arial", 15),width=20,cursor="hand2", relief="flat",command = login.destroy)
    btn_salir.pack()
    btn_salir.place(x=402,y=385)
    
    btn_volver= Button(image=img_net2, bg='#000000',font=("Arial", 15),text="Salir",width=50,cursor="hand2", relief="flat",command = volver)
    btn_volver.pack()
    btn_volver.place(x=10,y=5)
    btn_volver= Button(login, text="volver para iniciar secion", wraplength=100, fg='#FFFFFF' ,bg='#000000',font=("Arial", 13),height=2,width=11,cursor="hand2", relief="flat",command = volver)
    btn_volver.pack()
    btn_volver.place(x=60,y=5)


    mainloop()


def ir_l_m():
    login.destroy()
    import Menu

def volver():
    login.destroy()
    import inicio
    
def ir_l_f():
    login.destroy()
    import formulario 

fun_login()
