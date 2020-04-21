from pyfirmata import Arduino, util
from tkinter import *
from PIL import Image , ImageTk
from time import sleep

placa = Arduino ('COM3')
it = util.Iterator(placa)
#inicio el iteratodr
it.start()
analog_0= placa.get_pin('a:0:i') 
#analog_1= placa.get_pin('a:1:i') 

ventana = Tk()
ventana.geometry('1200x800')
ventana.configure(bg = 'white')
ventana.title("Bienvenidos a las UI")



Label(ventana, text="Valor ADC0 ").place(x=30, y=60)
dato=Label(ventana, text="0.0", bg='cadet blue1', font=("Arial Bold", 14), fg="white")
dato.place(x=40, y=90)
Label(ventana, text="Valor ADC1 ").place(x=150, y=60)
dato2=Label(ventana, text="0.0", bg='cadet blue2', font=("Arial Bold", 14), fg="white")
dato2.place(x=160, y=90)

title = Label(ventana,bg="RED", font=("Arial Bold", 14), fg="white")
title['text'] = "el titulo"
title.place(x = 300, y = 0)

mensaje1= Label(ventana,bg="RED", font=("Arial Bold", 14), fg="white")
mensaje2= Label(ventana,bg="RED", font=("Arial Bold", 14), fg="white")

mensaje3 = Label(ventana,bg="RED", font=("Arial Bold", 14), fg="white")
mensaje4 = Label(ventana,bg="RED", font=("Arial Bold", 14), fg="white")
mensaje5 = Label(ventana,bg="RED", font=("Arial Bold", 14), fg="white")



def medir():
    valor1 = analog_0.read()
    #valor2=analog_1.read()
    dato['text'] = str(valor1)
    # dato2['text'] = str(valor2)
    if(valor1>=0.5):
        mensaje1['text'] = "alerta ADC0"
        mensaje1.place(x = 70,y =130)  
        #mensaje3['text'] = "mensaje 1 de 3"
        mensaje3.place(x = 80, y = 200) 
        #mensaje4['text'] = "mensaje 2 de 3 "
        mensaje4.place(x = 80 , y = 240)
        #mensaje5['text'] = "mensaje 3 de 3 "
        mensaje5.place(x = 80, y = 280)
    elif(valor1<0.5):
        mensaje1.place_forget()
        mensaje3.place_forget()
        mensaje4.place_forget()
        mensaje5.place_forget()
    
while(1):
    medir()
    ventana.update()

ventana.mainloop()