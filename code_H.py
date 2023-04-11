from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
from operator import xor

window = Tk()
window.title("Código Hamming")
window.geometry("1200x550")
#window.resizable(False,False)
s = ttk.Style()
s.theme_use('clam')

label5 = Label(window, text="")
label6 = Label(window, text="")
table1 = ttk.Treeview(window, columns=("c1", "c2", "c3", "c4", "c5", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15"),
					  show='headings', height=6)
table2 = ttk.Treeview(window, columns=("c1", "c2", "c3", "c4", "c5", "c5", "c6", "c7", "c8", "c9", "c10", "c11","c12","c13","c14","c15","c16","c17","c18","c19"),
					  show='headings', height=5)
label3 = Label(window, text="")


def clear_all():
   for item in table1.get_children():
      table1.delete(item)
   for item in table2.get_children():
      table2.delete(item)
    

def clear_all2():
   for item in table2.get_children():
      table2.delete(item)



def binario_a_decimal(numero_binario):
	numero_decimal = 0

	for posicion, digito_string in enumerate(numero_binario[::-1]):
		numero_decimal += int(digito_string) * 2 ** posicion

	return numero_decimal

#BOTON 1
def codificacion():
	global data
	clear_all()
	data = entry1.get()
	m = len(data)
	

	if m<11 or m>11:
		MessageBox.showinfo("Dato", "El dato no es de 11 bits, ingrese el dato nuevamente")
	else:
		global p1,p2,p3,p4
		p1 = xor(int(data[0]), xor(int(data[1]), xor(int(data[3]), xor(int(data[4]),xor(int(data[6]), xor(int(data[8]),int(data[10])))) )))
		# print(p1)
		p2 = xor(int(data[0]), xor(int(data[2]), xor(int(data[3]), xor(int(data[5]), xor(int(data[6]), xor(int(data[9]), int(data[10])))))))
		# print(p2)
		p3 = xor(int(data[1]), xor(int(data[2]), xor(int(data[3]), xor(int(data[7]),xor(int(data[8]),xor(int(data[9]),int(data[10])))))))
		# print(p3)
		p4 = xor(int(data[4]), xor(int(data[5]), xor(int(data[6]),xor(int(data[7]),xor(int(data[8]),xor(int(data[9]), int(data[10])))))))
		# print(p4)

		datPar=[p1,p2,data[0],p3,data[1],data[2],data[3],p4,data[4],data[5],data[6],data[7],data[8],data[9],data[10]]

		table1.column("# 1", anchor=CENTER,stretch=NO)
		table1.heading("# 1", text="")
		table1.column("# 2", anchor=CENTER, width=50)
		table1.heading("# 2", text="p1")
		table1.column("# 3", anchor=CENTER, width=50)
		table1.heading("# 3", text="p2")
		table1.column("# 4", anchor=CENTER, width=50)
		table1.heading("# 4", text="d1")
		table1.column("# 5", anchor=CENTER,width=50)
		table1.heading("# 5", text="p3")
		table1.column("# 6", anchor=CENTER, width=50)
		table1.heading("# 6", text="d2")
		table1.column("# 7", anchor=CENTER, width=50)
		table1.heading("# 7", text="d3")
		table1.column("# 8", anchor=CENTER, width=50)
		table1.heading("# 8", text="d4")
		table1.column("# 9", anchor=CENTER, width=50)
		table1.heading("# 9", text="p4")
		table1.column("# 10", anchor=CENTER, width=50)
		table1.heading("# 10", text="d5")
		table1.column("# 11", anchor=CENTER, width=50)
		table1.heading("# 11", text="d6")
		table1.column("# 12", anchor=CENTER, width=50)
		table1.heading("# 12", text="d7")
		table1.column("# 13", anchor=CENTER, width=50)
		table1.heading("# 13", text="d8")
		table1.column("# 14", anchor=CENTER, width=50)
		table1.heading("# 14", text="d9")
		table1.column("# 15", anchor=CENTER, width=50)
		table1.heading("# 15", text="d10")
		table1.column("# 16", anchor=CENTER, width=50)
		table1.heading("# 16", text="d11")
		
		
		



		#                                   ,p1,p2,d1,p3,d2,d3,d4,p4,d5,d6,d7
		table1.insert("", END, text="Palabra de datos(sin paridad)", values=("Palabra de datos(sin paridad)","","",
					str(data[0]),"",str(data[1]),str(data[2]),str(data[3]),"",str(data[4]),str(data[5]),str(data[6]), str(data[7]), str(data[8]), str(data[9]), str(data[10])))
		table1.insert("", END, text="p1", values=("p1", str(p1), "", str(data[0]),"",str(data[1]),"",str(data[3]),"",str(data[4]),"",str(data[6]),"",str(data[8]),"",str(data[10])))
		table1.insert("", END, text="p2", values=("p2", "",str(p2),str(data[0]),"","",str(data[2]),str(data[3]),"","",str(data[5]),str(data[6]),"","",str(data[9]),str(data[10])))
		table1.insert("", END, text="p3", values=("p3", "","","",str(p3),str(data[1]),str(data[2]),str(data[3]),"","","","",str(data[7]),str(data[8]),str(data[9]),str(data[10])))
		table1.insert("", END, text="p4", values=("p4", "","","","","","","",str(p4),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(data[9]), str(data[10])))
		table1.insert("", END, text="Palabra de datos(con paridad)", values=("Palabra de datos(con paridad)",str(datPar[0]),str(datPar[1]),str(datPar[2])
											,str(datPar[3]),str(datPar[4]),str(datPar[5]),str(datPar[6]),str(datPar[7]),str(datPar[8]),str(datPar[9]),str(datPar[10]),str(datPar[11]),str(datPar[12]),str(datPar[13]),str(datPar[14])))
		table1.pack()

#BOTON 2
def error():

	clear_all2()
	global label3
	label3.pack_forget()


	data = entry1.get()
	m2=len(data)
	global arr1
	arr1 = entry2.get()


	m2 = len(arr1)

	if m2<11 or m2>11:
		MessageBox.showinfo("Dato", "El dato no es de 11 bits, ingrese el dato nuevamente")
	else:
		"""            #d1            #d2               #d4               #d5                #d7
		p1 = xor(int(data[0]), xor(int(data[1]), xor(int(data[3]), xor(int(data[4]), int(data[6])))))
		# print(p1)
					# d1            #d3               #d4               #d6                #d7
		p2 = xor(int(data[0]), xor(int(data[2]), xor(int(data[3]), xor(int(data[5]), int(data[6])))))
		# print(p2)
					# d2           #d3               #d4
		p3 = xor(int(data[1]), xor(int(data[2]), int(data[3])))
		# print(p3)
					# d5            #d6               #d7
		p4 = xor(int(data[4]), xor(int(data[5]), int(data[6])))
		


		p5 = xor(int(arr1[0]), xor(int(arr1[1]), xor(int(arr1[3]), xor(int(arr1[4]), int(arr1[6])))))
		# print(p1)
		p6 = xor(int(arr1[0]), xor(int(arr1[2]), xor(int(arr1[3]), xor(int(arr1[5]), int(arr1[6])))))
		# print(p2)
		p7 = xor(int(arr1[1]), xor(int(arr1[2]), int(arr1[3])))
		# print(p3)
		p8 = xor(int(arr1[4]), xor(int(arr1[5]), int(arr1[6])))"""
		p5 = xor(int(arr1[0]), xor(int(arr1[1]), xor(int(arr1[3]), xor(int(arr1[4]),xor(int(arr1[6]), xor(int(arr1[8]),int(arr1[10])))) )))
		# print(p1)
		p6 = xor(int(arr1[0]), xor(int(arr1[2]), xor(int(arr1[3]), xor(int(arr1[5]), xor(int(arr1[6]), xor(int(arr1[9]), int(arr1[10])))))))
		# print(p2)
		p7 = xor(int(arr1[1]), xor(int(arr1[2]), xor(int(arr1[3]), xor(int(arr1[7]),xor(int(arr1[8]),xor(int(arr1[9]),int(arr1[10])))))))
		# print(p3)
		p8 = xor(int(arr1[4]), xor(int(arr1[5]), xor(int(arr1[6]),xor(int(arr1[7]),xor(int(arr1[8]),xor(int(arr1[9]), int(arr1[10])))))))
		# print(p4)
		if p1 != p5:
			e1="Error(1)"
			f1="1"
		else:
			e1="Correcto(0)"
			f1="0"
		if p2 != p6:
			e2 = "Error(1)"
			f2="1"
		else:
			e2="Correcto(0)"
			f2="0"
		if p3 != p7:
			e3="Error(1)"
			f3="1"
		else:
			e3="Correcto(0)"
			f3="0"
		if p4 != p8:
			e4 = "Error(1)"
			f4="1"
		else:
			e4="Correcto(0)"
			f4="0"

		label3 = Label(window, text="")
		comp=str(f4+f3+f2+f1)
		print(comp)
		poserror = binario_a_decimal(comp)
		print("error",poserror)
		"""
		if poserror != 0 and poserror != 3 and poserror != 5 and poserror !=6 and poserror !=7 and poserror !=9 and poserror !=10 and poserror !=11:
			MessageBox.showinfo("Dato", "El código solo permite detedctar un error, digite nuevamente")
			return
		else:
			poserror1=poserror
			"""

		table2.column("# 1", anchor=CENTER,stretch=NO)
		table2.heading("# 1", text="")
		table2.column("# 2", anchor=CENTER, width=40)
		table2.heading("# 2", text="p1")
		table2.column("# 3", anchor=CENTER, width=40)
		table2.heading("# 3", text="p2")
		table2.column("# 4", anchor=CENTER, width=40)
		table2.heading("# 4", text="d1")
		table2.column("# 5", anchor=CENTER,width=40)
		table2.heading("# 5", text="p3")
		table2.column("# 6", anchor=CENTER, width=40)
		table2.heading("# 6", text="d2")
		table2.column("# 7", anchor=CENTER, width=40)
		table2.heading("# 7", text="d3")
		table2.column("# 8", anchor=CENTER, width=40)
		table2.heading("# 8", text="d4")
		table2.column("# 9", anchor=CENTER, width=40)
		table2.heading("# 9", text="p4")
		table2.column("# 10", anchor=CENTER, width=40)
		table2.heading("# 10", text="d5")
		table2.column("# 11", anchor=CENTER, width=40)
		table2.heading("# 11", text="d6")
		table2.column("# 12", anchor=CENTER, width=40)
		table2.heading("# 12", text="d7")
		table2.column("# 13", anchor=CENTER, width=40)
		table2.heading("# 13", text="d8")
		table2.column("# 14", anchor=CENTER, width=40)
		table2.heading("# 14", text="d9")
		table2.column("# 15", anchor=CENTER, width=40)
		table2.heading("# 15", text="d10")
		table2.column("# 16", anchor=CENTER, width=40)
		table2.heading("# 16", text="d11")
		
		table2.column("# 17", anchor=CENTER, width=60)
		table2.heading("# 17", text="Paridad 1")
		table2.column("# 18", anchor=CENTER,width=60)
		table2.heading("# 18", text="Paridad 2")
		table2.column("# 19", anchor=CENTER,width=90)
		table2.heading("# 19", text="Comprobación")

									#                                   ,p1,p2,d1,p3,d2,d3,d4,p4,d5,d6,d7,d8,d9,d10
		table2.insert("", END, text="Palabra de datos recibida", values=("Palabra de datos(sin paridad)","","",
					str(arr1[0]),"",str(arr1[1]),str(arr1[2]),str(arr1[3]),"",str(arr1[4]),str(arr1[5]),str(arr1[6]),str(arr1[7]),str(arr1[8]),str(arr1[9]),str(arr1[10])))
		table2.insert("", END, text="p1", values=("p1", str(p5), "", str(arr1[0]),"",str(arr1[1]),"",str(arr1[3]),"",str(arr1[4]),"",str(arr1[6]),"",str(arr1[8]),"",str(arr1[10]),str(p5),str(p1),e1))
		table2.insert("", END, text="p2", values=("p2", "",str(p6),str(arr1[0]),"","",str(arr1[2]),str(arr1[3]),"","",str(arr1[5]),str(arr1[6]),"","",str(arr1[9]),str(arr1[10]),str(p6),str(p2),e2))
		table2.insert("", END, text="p3", values=("p3", "","","",str(p7),str(arr1[1]),str(arr1[2]),str(arr1[3]),"","","","",str(arr1[7]),str(arr1[8]),str(arr1[9]),str(arr1[10]),str(p7),str(p3),e3))
		table2.insert("", END, text="p4", values=("p4", "","","","","","","",str(p8),str(arr1[4]),str(arr1[5]),str(arr1[6]),str(arr1[7]),str(arr1[8]),str(arr1[9]),str(arr1[10]),str(p8),str(p4),e4))
		"""
		table1.insert("", END, text="Palabra de datos(sin paridad)", values=("Palabra de datos(sin paridad)","","",
					str(data[0]),"",str(data[1]),str(data[2]),str(data[3]),"",str(data[4]),str(data[5]),str(data[6]), str(data[7]), str(data[8]), str(data[9]), str(data[10])))
		table2.insert("", END, text="p1", values=("p1", str(p5), "", str(data[0]),"",str(data[1]),"",str(data[3]),"",str(data[4]),"",str(data[6]),"",str(data[8]),"",str(data[10])))
		table2.insert("", END, text="p2", values=("p2", "",str(p2),str(data[0]),"","",str(data[2]),str(data[3]),"","",str(data[5]),str(data[6]),"","",str(data[9]),str(data[10])))
		table2.insert("", END, text="p3", values=("p3", "","","",str(p3),str(data[1]),str(data[2]),str(data[3]),"","","","",str(data[7]),str(data[8]),str(data[9]),str(data[10])))
		table2.insert("", END, text="p4", values=("p4", "","","","","","","",str(p4),str(data[4]),str(data[5]),str(data[6]),str(data[7]),str(data[8]),str(data[9]), str(data[10])))
		table2.insert("", END, text="Palabra de datos(con paridad)", values=("Palabra de datos(con paridad)",str(datPar[0]),str(datPar[1]),str(datPar[2])
	
    
    
        """



		table2.pack()
		label3 = Label(window, text=f"El error está en el dato de la posición: {poserror}")
		label3.config(font=("helvetica", 12))
		label3.pack()

label1 = Label(window, text='Ingrese el dato a transmitir: ')
label1.pack()
entry1 = Entry(window)
entry1.pack()
label1.config(font=('helvetica', 12))

button1 = Button(text='OK', command=codificacion, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
button1.pack()

label2 = Label(window, text='Ingrese el dato con error: ')
label2.pack()
entry2 = Entry(window)
entry2.pack()
label2.config(font=('helvetica', 12))

button1 = Button(text='OK', command=error, bg='black', fg='white',font=('helvetica', 10, 'bold'))
button1.pack()
button3 = Button(text='Clear', command=clear_all, bg='brown', fg='white',font=('helvetica', 10, 'bold'))
button3.pack()

window.mainloop() 