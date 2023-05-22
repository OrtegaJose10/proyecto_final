import tkinter as tk

# Base de datos de alimentos con sus precios
menu = {
    "Salados": {
        "Hamburguesa": 10.99,
        "Pizza": 8.99,
        "Ensalada": 5.99
    },
    "Bebidas": {
        "Refresco": 1.99,
        "Agua": 0.99,
        "Jugo": 2.99
    },
    "Bebidas Alcohólicas": {
        "Cerveza": 4.99,
        "Vino": 9.99,
        "Whisky": 12.99
    },
    "Meriendas": {
        "Papas fritas": 3.99,
        "Nachos": 4.99,
        "Empanadas": 2.49
    },
    "Postres": {
        "Helado": 3.99,
        "Pastel": 5.99,
        "Frutas": 2.99
    }
}

# Función para calcular el costo total del pedido
def calcular_total():
    total = 0.0
    for item in pedido_listbox.get(0, tk.END):
        for category, foods in menu.items():
            if item in foods:
                total += foods[item]
    total_label.config(text=f"Total a pagar: ${total:.2f}")

# Función para agregar el alimento seleccionado al pedido
def agregar_alimento():
    selected_item = alimentos_listbox.get(tk.ACTIVE)
    pedido_listbox.insert(tk.END, selected_item)
    calcular_total()

# Función para eliminar el alimento seleccionado del pedido
def eliminar_alimento():
    selected_index = pedido_listbox.curselection()
    if selected_index:
        pedido_listbox.delete(selected_index)
        calcular_total()

# Crear la ventana principal
window = tk.Tk()
window.title("Restaurante")

# Crear el listbox de las categorías de alimentos
categorias_frame = tk.Frame(window)
categorias_frame.pack(side=tk.LEFT, padx=10)
categorias_label = tk.Label(categorias_frame, text="Categorías")
categorias_label.pack()
categorias_listbox = tk.Listbox(categorias_frame, selectmode=tk.SINGLE)
categorias_listbox.pack()

# Agregar las categorías al listbox de categorías
for category in menu:
    categorias_listbox.insert(tk.END, category)

# Crear el listbox de los alimentos y precios
alimentos_frame = tk.Frame(window)
alimentos_frame.pack(side=tk.LEFT, padx=10)
alimentos_label = tk.Label(alimentos_frame, text="Alimentos y Precios")
alimentos_label.pack()
alimentos_listbox = tk.Listbox(alimentos_frame, selectmode=tk.SINGLE)
alimentos_listbox.pack()

# Función para actualizar los alimentos y precios según la categoría seleccionada
def actualizar_alimentos(event):
    alimentos_listbox.delete(0, tk.END)
    selected_category = categorias_listbox.get(tk.ACTIVE)
    for food, price in menu[selected_category].items():
        alimentos_listbox.insert(tk.END, f"{food}: ${price:.2f}")

categorias_listbox.bind("<<ListboxSelect>>", actualizar_alimentos)

# Crear el listbox del pedido
pedido_frame = tk.Frame(window)
pedido_frame.pack(side=tk.LEFT, padx=10)
pedido_label = tk.Label(pedido_frame, text="Pedido")
pedido_label.pack()
pedido_listbox = tk.Listbox(pedido_frame)
pedido_listbox.pack()

# Crear el botón para agregar alimento al pedido
agregar_button = tk.Button(window, text="Agregar", command=agregar_alimento)
agregar_button.pack(pady=5)

# Crear el botón para eliminar alimento del pedido
eliminar_button = tk.Button(window, text="Eliminar", command=eliminar_alimento)
eliminar_button.pack(pady=5)

# Crear el botón para calcular el total
calcular_button = tk.Button(window, text="Calcular Total", command=calcular_total)
calcular_button.pack(pady=5)

# Crear la etiqueta para mostrar el total a pagar
total_label = tk.Label(window, text="Total a pagar: $0.00")
total_label.pack()

# Ejecutar el programa
window.mainloop()
