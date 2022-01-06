#SE DEBERAN FORMAR 144FILAS Y 96 COLUMNAS
#NOTA EL CONCAT VERTICAL DE CV2, es de arroba hacia abajo
#13824 imagenes
#cada columna de 96imagenes
#144 filas

import numpy as np
import matplotlib.pyplot as plt

rutapc ="C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST2/F"
rutalap ="D:/Modular/CODE 2 GEN/IMAGES/TEST/F"

def loadImagesC(verticalLenght,filaPos):#idealmente seran 96 por columna
    imagesC=[]
    fila=filaPos

    for i in range(1,verticalLenght+1):
        imagesC.append(np.loadtxt(f"C:/Users/Javier/Documents/INCO/MODULAR/IMAGES/TEST/F{fila}-C{i}_file.txt").reshape(5, 5))
    return imagesC


                    #^columzise  #>filasize       #
def loadColumnsRF(verticalLength,horizontalLength,filaPos):
    column=[]
    fila=filaPos

    for i in range (1,horizontalLength+1):
        images =loadImagesC(verticalLength,i)
        column.append(np.vstack([*images]))

    return column

def showFinalImage(filas):
    finalImage = np.hstack([*filas])
    fig, ax = plt.subplots()

    plt.axis('off')

    ax.imshow(finalImage)
    fig.savefig('final.png', bbox_inches='tight', pad_inches=0,dpi=15)
    plt.show()

    


        