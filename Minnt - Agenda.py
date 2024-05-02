#agenda
#Omar Alejandro Galvis Espitia  02/05/2024

nom = ["alejandro","liliana","elizabeth","omar","copito"]
num = ["3125577909","4454625035","3546879584","3159876501","3180457900"]
eda = ["21","23","20","22","19"]

while(True):
    opc = int(input("1. Contactos \n2. Agregar contacto \n3. Eliminar contacto \n4. Editar contacto \n"))
    if opc == 1:
        print("Contactos:")
        print(nom)
        ind = int(input("Ingrese un numero:"))
        print("Nombre:", nom[ind] )
        print("Telefono:", num[ind])
        print("Edad", eda[ind])
    elif opc == 2:
        print("Agregar Contacto:")
        nnom = str(input("Ingrese un nombre: "))
        nnum = int(input("Ingrese el numero de telefono: "))
        neda = int(input("Ingrese la edad: "))
        nom.append(nnom)
        num.append(nnum)
        eda.append(neda)
        print("El contacto fue agregado!")
    elif opc == 3:
        print("Eliminar Contacto:")
        print(nom)
        nnom = str(input("Elige un nombre: "))
        nnum = int(input("Elige el numero de telefono: "))
        neda = int(input("Elige la edad: "))
        nom.pop(nnom)
        num.pop(nnum)
        eda.pop(neda)
        print("El contacto fue eliminado!")
        print(nom)
    elif opc == 4:
        print("Editar Contacto:")
        print(nom)
        ind = int(input("Seleccione un contacto:"))
        enom = str(input("Nombre nuevo: "))
        nom[ind] = enom
        enum = int(input("Telefono nuevo: "))
        num[ind] = enum
        eeda = int(input("Edad: "))
        eda[ind] = eeda
    else:
        print("Opcion invalida")
