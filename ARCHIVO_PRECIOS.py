def LeerArchivoPrecios(ruta):
    #creo el diccionario
    diccionario={}
    #abro el archivo para extraer la info.
    with open (ruta,"r") as file:
        #leo el archivo
        lineas=file.readlines()
        #recorro cada linea del archivo
        for i in range(len(lineas)) :
            #elimino los saltos de linea para evitar errores
            lineas[i]=lineas[i].replace("\n","")
            #utilizo las lineas del archivo para crear una lista con sus elementos
            #se separa la linea en elementos segun sus comas (funcion split())
            lineas[i]=lineas[i].split(",")
            #creo un nuevo elemento en el diccionario utilizando como llave el primer elemento
            #de la lista, y como valor creo un diccionario para almacenar el resto de valores
            diccionario[lineas[i][0]]={}
            #recorro las listas que obtuve al dividir las lineas, sin contar los primeros 
            #elementos (los modelos)
            for j in range(1,len(lineas[i])):
                #separo los elementos por la clave y el valor (separados en el archivo por ":")
                llaveValor=lineas[i][j].split(":")
                #creo un nuevo elemento en el diccionario que corresponde al modelo, utilizando
                #como llave el nombre de lo que se desea reparar(llaveValor[0]) y como valor 
                #utilizo el valor que le corresponde(llaveValor[1])
                diccionario[lineas[i][0]][llaveValor[0]]=llaveValor[1]
        return diccionario
if __name__=="__main__":
    ruta="Precios.txt"
    diccionario=LeerArchivoPrecios(ruta)
    print(diccionario)
    #ejemplo de ejecucion
    print(diccionario["iPhone 7"]["Modulo"])