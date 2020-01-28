datoBuscar = input("INGRESE EL DATO A BUSCAR: ")
print(datoBuscar)

import os

def all_word_pairs(directorio):
	filenames = []
	for file in os.listdir(directorio):
		if file.endswith(".txt"):
			filenames.append(file)
	return lines(filenames)

def lines(filename):
    print("NOMBRE DE LOS ARCHIVOS: ",filename)
    words = []
    i = 0
    while i < len(filename):
        filename[i] = 'Ruta de los archivos'+filename[i]
        #filename[i] = 'D://Python//docuemntos//' + filename[i]
        with open(filename[i]) as f:
            for w in f:
                words.append(w[0:len(w) - 1])
        #print("CONTENIDO DEL ARCHIVO: ",words)
        search(words,datoBuscar)
        words = []
        i = i + 1

def search(list,dato):
    print("DATO BUSCAR: ",dato)
    print("CONTENIDO DEL ARCHIVO: ",list)

all_word_pairs('Ruta de los archivos')
#all_word_pairs('D://Python//docuemntos')
#lines(all_word_pairs('Ruta de los archivos'))