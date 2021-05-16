# -*- coding: utf-8 -*-
"""
Created on Fri May 14 21:09:16 2021

@author: Geoffrey Hernandez 
"""

import PySimpleGUI as sg


sg.theme('BluePurple')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Proyecto 1')],
            [sg.Text('Geoffrey Hernandez 7090-14-3807')],
            [sg.Text('ENTRADA, n1, n2'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('AMBAS, n2, n3'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('AMBAS, n3, n4'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('SALIDA, n4, n5'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('AMBAS, n7, n2'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('AMBAS, n7, n4'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('ENTRADA, n6, n7'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('AMBAS, n7, n8'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Text('SALIDA, n8, n9'), sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50"),sg.InputText(size="50")],
            [sg.Button('Generar PDF de Grafos'), sg.Button('Salir')] ]

# Create the Window
window = sg.Window('Window Title', layout)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break    
    
 
    file = open("arrayaristas.txt", "w")
    file.write("ENTRADA, n1, n2, "+values[0]+","+" "+values[1]+","+" "+values[2]+","+" "+values[3]+","+" "+values[4]+","+" "+values[5]+'\n')
    file.write("AMBAS, n2, n3, "+values[6]+","+" "+values[7]+","+" "+values[8]+","+" "+values[9]+","+" "+values[10]+","+" "+values[11]+'\n')
    file.write("AMBAS, n3, n4, "+values[12]+","+" "+values[13]+","+" "+values[14]+","+" "+values[15]+","+" "+values[16]+","+" "+values[17]+'\n')
    file.write("SALIDA, n4, n5, "+values[18]+","+" "+values[19]+","+" "+values[20]+","+" "+values[21]+","+" "+values[22]+","+" "+values[23]+'\n')
    file.write("AMBAS, n7, n2, "+values[24]+","+" "+values[25]+","+" "+values[26]+","+" "+values[27]+","+" "+values[28]+","+" "+values[29]+'\n')
    file.write("AMBAS, n7, n4, "+values[30]+","+" "+values[31]+","+" "+values[32]+","+" "+values[33]+","+" "+values[34]+","+" "+values[35]+'\n')
    file.write("ENTRADA, n6, n7, "+values[36]+","+" "+values[37]+","+" "+values[38]+","+" "+values[39]+","+" "+values[40]+","+" "+values[41]+'\n')
    file.write("AMBAS, n7, n8, "+values[42]+","+" "+values[43]+","+" "+values[44]+","+" "+values[45]+","+" "+values[46]+","+" "+values[47]+'\n')
    file.write("SALIDA, n8, n9, "+values[48]+","+" "+values[49]+","+" "+values[50]+","+" "+values[51]+","+" "+values[52]+","+" "+values[53])
    file.close()
    import os
    os.system('python Proyecto1.py')

window.close()

