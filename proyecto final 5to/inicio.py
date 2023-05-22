from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


def fun_menu():
    global menu
    menu = Tk()
    menu.title("Bienvenidos")
    menu.resizable(0,0)
    menu.geometry("1110x470")  #ancho, alto

    img_net = Image.open("Imagenes/logo1.png")

    resized = img_net.resize((500,300))
    img_net = ImageTk.PhotoImage(resized)

    label_imagen = Label(menu, image = img_net, bg='#FFFFFF')
    label_imagen.pack()
    label_imagen.place(x=10, y=113)
    
    img_net1 = Image.open("Imagenes/usuario2.png")

    resized = img_net1.resize((684,355))
    img_net1 = ImageTk.PhotoImage(resized)

    label_imagen = Label(menu, image = img_net1, bg='black')
    label_imagen.pack()
    label_imagen.place(x=450, y=23)
    
    menu.configure(bg='black')

    lbl_registrese = Label(menu, text= "  USUARIO  ", fg='white', bg='black')
    lbl_registrese.configure(font=("Arial Black", 50))
    lbl_registrese.pack()
    lbl_registrese.place(x=10, y=40)

    btn_iniciar_sesion= Button(menu, text= "      INICIE SECION      ", bg='#FFFFFF',font=("Arial", 13),width=15,height=1, relief="flat", cursor="hand2",command = fun_login)
    btn_iniciar_sesion.pack()
    btn_iniciar_sesion.place(x=824,y=248)
    #tamaño del boton= (,height=2,width=20)
    btn_registrarse= Button(menu, text= "      REGISTRARSE      ", bg='#FFFFFF',font=("Arial", 13),width=15,height=1, relief="flat", cursor="hand2",command = ir_l_m)
    btn_registrarse.pack()
    btn_registrarse.place(x=615,y=248)
    
    btn_salir= Button(menu, text= "      SALIR      ", bg='#FFFFFF',font=("Arial", 13),width=15,height=1, relief="flat", cursor="hand2",command = menu.destroy)
    btn_salir.pack()
    btn_salir.place(x=715,y=340)

    mainloop()


def ir_l_m():
    menu.destroy()
    import login


def fun_login():
    menu.destroy()
    import login

def fun_login():
    menu.destroy()
    import login



fun_menu()
