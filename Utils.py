import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
import numpy as np
import scipy.signal

def extraccionDatosOnda(baseDatos, window_max, agregado = ""):
    dato_graf = {} #sn diccionarios 
    dato_calc = {}
    
    for señal_n in range(baseDatos.values.shape[0]):
        #print("Procesando señal", señal_n)
        
        señal = baseDatos.values[señal_n]
        #señal = baseDatos.iloc[señal_n].values
        
        recorteB = señal[:window_max] #ver si cambiar por window = np.zeros(señal.shape[0]) y window[:window_max] = 1.0
        
        peaks, properties = scipy.signal.find_peaks(recorteB, prominence=5000, width=40, distance=500)
        
        if peaks.size <= 0:
            peaks = recorteB.argmax()[np.newaxis] #np.newaxis le agrega un eje al array que te devuelve argmax que es necesario para compatibilidad. Argmax(), es el valor en X, que representa el pico maximo en la señal.        
        
        anchosB = scipy.signal.peak_widths(recorteB, peaks, rel_height=0.8)
        
        try: #ene stas funciones saca el peaks de scipy.signal.find_peaks
            dato_graf["yOndaB" + agregado].append(recorteB[peaks[0]]) #Y(peaks)
            dato_calc["LATENCIA ONDA B" + agregado].append(peaks[0])

            dato_calc["AMPLITUD ONDA B" + agregado].append(abs(recorteB[peaks[0]] - recorteB[0])) #Y(peaks)-Y(0)
            dato_calc["ANCHO ONDA B" + agregado].append(anchosB[0][0]) #El valor del ancho se obtiene en un vector de 4 valores.

            dato_graf["anchoB1"+ agregado].append(anchosB[1][0])
            dato_graf["anchoB2"+ agregado].append(anchosB[2][0])
            dato_graf["anchoB3"+ agregado].append(anchosB[3][0])
        
        except KeyError:
            dato_graf["yOndaB" + agregado] = [recorteB[peaks[0]]] # en todas estas funciones except, saco el peaks del if
            dato_calc["LATENCIA ONDA B" + agregado]= [peaks[0]]

            dato_calc["AMPLITUD ONDA B" + agregado] = [abs(recorteB[peaks[0]] - recorteB[0])]
            dato_calc["ANCHO ONDA B" + agregado] = [anchosB[0][0]]

            dato_graf["anchoB1"+ agregado] = [anchosB[1][0]]
            dato_graf["anchoB2"+ agregado] = [anchosB[2][0]]
            dato_graf["anchoB3"+ agregado] = [anchosB[3][0]]
            
        #extraer onda A entre 0 y picoB
        
        recorteA = señal[:peaks[0]] #peaks de la onda B ver si cambiar por window = np.zeros(señal.shape[0]) y window[:latencia_b] = 1.0
        
        if recorteA.shape[0] == 0: #se realizo por una sola funcion que empezaba en 0 y ese era su pico maximo 
            peaks = np.array([0])
            anchosA=[[0],[0],[0],[0]]
            recorteA = señal[0:1]
        else:
            peaks, properties = scipy.signal.find_peaks((-1)*recorteA, prominence=1, width=10, distance=500)
        
            if peaks.size <= 0:
                peaks = recorteA.argmin()[np.newaxis] #np.newaxis le agrega un eje al array que te devuelve argmax que es necesario para compatibilidad

            anchosA = scipy.signal.peak_widths((-1)*recorteA, peaks, rel_height=1.0)
        
        try:
            dato_graf["yOndaA" + agregado].append(recorteA[peaks[0]])

            dato_calc["LATENCIA ONDA A" + agregado].append(peaks[0])

            dato_calc["AMPLITUD ONDA A" + agregado].append(abs(recorteA[peaks[0]] - recorteA[0]))

            dato_calc["ANCHO ONDA A" + agregado].append(anchosA[0][0])

            dato_graf["anchoA1"+ agregado].append(anchosA[1][0])
            dato_graf["anchoA2"+ agregado].append(anchosA[2][0])
            dato_graf["anchoA3"+ agregado].append(anchosA[3][0])
            
        except KeyError:
            dato_graf["yOndaA" + agregado] = [recorteA[peaks[0]]]

            dato_calc["LATENCIA ONDA A" + agregado] = [peaks[0]]

            dato_calc["AMPLITUD ONDA A" + agregado] = [abs(recorteA[peaks[0]] - recorteA[0])]

            dato_calc["ANCHO ONDA A" + agregado] = [anchosA[0][0]]

            dato_graf["anchoA1"+ agregado] = [anchosA[1][0]]
            dato_graf["anchoA2"+ agregado] = [anchosA[2][0]]
            dato_graf["anchoA3"+ agregado] = [anchosA[3][0]]
        
    return pd.DataFrame.from_dict(dato_calc), pd.DataFrame.from_dict(dato_graf)

def scan_folders(direc, nivel = 0, full_file_list=None,extension=".TXT"): #ingreso direccion,  nivel=0 que va recorriendo niveles,ull_file_list vacia que va juntando los datos 
    
    if full_file_list is None:
        full_file_list = []

    elem_list = os.listdir(direc) #Identifica lo que hay en la carpeta señales ERG
    file_list = [] #lista vacia de archivos
    folder_list = [] #lista vacia de carpetas

    for e in elem_list:
        if "." in e: #recorro los elementos de la primera linea de clasificacion
            file_list.append(e) #si hay un punto en esos elementos apendeo en la lista de archivos
        else:
            folder_list.append(e) #sino apendeo en lista de carpetas
    
    for files in file_list: # recorro la lista de archivos
        if extension in files: # si hay archivos txt en la carpeta de archivos 
            temp_list = [] #crea una lista temporal vacia para en lo que sigue agregar el split de la direccion
            for n in range(nivel, -1, -1): # range(start, stop, step), de lo mas chico a lo mas grande
                temp_list.append(direc.split("/")[-1-n]) #divide en las barras y toma la parte final de la direccion. Toma el split de la direccion en un nivel cada vez mas atras 
            temp_list.append(files)# apendea en la lista temporal archivo recorrido
            full_file_list.append(temp_list) #apendea en la lista full lo que hay en el temporal o sea voy a tener el nombre del archivo
        
    if len(folder_list) > 0: # se fija longitud de la lista de carpetas y si es mayor a 0 la escanea 
        for f in folder_list: # recorre la lista de carpetas
            scan_folders(direc+"/"+f, nivel+1, full_file_list) 
    else:
        None
        
    return(full_file_list)

