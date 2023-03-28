import tkinter as tk
import pandas as pd
import tabulate as tb
import matplotlib.pyplot as plt
import numpy as np

binary_string=""

def send():
    hexa_num = entry.get()
    print(hex_to_dec(hexa_num))
    print(hex_to_oct(hexa_num))
    print(hex_to_bin(hexa_num))
    binary_string = hex_to_bin(hexa_num)
    plot_NRZI(binary_string)
    
def es_hexadecimal(numero):
    """
    Función que valida si un número dado es hexadecimal.
    Retorna True si el número es hexadecimal, False si no lo es.
    """
    try:
        int(numero, 16)
        return True
    except ValueError:
        return False

def hex_to_dec(hex_num):
    return int(hex_num, 16)

def hex_to_oct(hex_num):
    decimal_num = int(hex_num, 16)
    octal_num = oct(decimal_num)
    return octal_num[2:]

def hex_to_bin(hex_num):
    decimal_num = int(hex_num, 16)
    binary_num = bin(decimal_num)
    return binary_num[2:]

def separar_digitos(numero):
    lista_digitos = []
    for digito in str(numero):
        lista_digitos.append(int(digito))
    return lista_digitos

def plot_NRZI(binary_string):
    """
    Plot the Non-Return-to-Zero Inverted (NRZI) signal for a given binary string.
    """
    signal_0 = []
    previous_bit = -1

    for bit in binary_string:
        if bit == '1':
            signal_0.append(previous_bit * -1)
            previous_bit = signal_0[-1]
        else:
            signal_0.append(previous_bit)
    
    signal = [0]
    for elemento in signal_0:
        if elemento == 1:
            signal.append(elemento)
        else:
            signal.append(0)
    
    # plot the signal
    fig, ax = plt.subplots()
    ax.step(range(len(signal)), signal, where='post', color='blue')
    ax.set_title('NRZI Signal')
    ax.set_xlabel('Bit')
    ax.set_ylabel('Signal Level')
    ax.set_ylim([-0.5, 1.5])
    plt.show()

# Crea una ventana principal
root = tk.Tk()
root.title("Interfaz con entrada de texto y botón")
root.geometry("300x300")

# Crea una etiqueta y una entrada de texto
label = tk.Label(root, text="Ingrese su texto:")
label.pack()
entry = tk.Entry(root)
entry.pack()

# Crea un botón y lo vincula a la función "mostrar_texto"
button = tk.Button(root, text="Enviar", command=send)
button.pack()

# Inicia el bucle de eventos principal
root.mainloop()
