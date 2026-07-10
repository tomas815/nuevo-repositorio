#diccionario para guardar la informacion de las peliculas
peliculas = {
    "p101": ["Luz de Otoño", "drama", 110, "B", "Español", False],
    "p102": ["Noche Neón", "acción", 125, "C", "Ingles", True],
    "p103": ["Planeta Agua", "documental", 90, "A", "Español", False],
    "p104": ["Risa Total," "comedia", 105, "A", "Español", True],
    "p105": ["Codigo Zero", "Triller", 118, "c", "Ingles", True],
    "p106": ["Viaje Lunar", "ciencia ficcion", 132, "B", "Ingles", False],
}
#diccionario para guardar el precio y cupos de las peliculas
cartelera = {
    "p101": [5990, 40],
    "p102": [7990, 0],
    "p103": [4990, 25],
    "p104": [6990, 12],
    "p105": [8990, 8],
    "p106": [7490, 3],
}
#funcion para mostrar el menu y sus opciones
def menu():
    print("==== MENÚ PRINCIPAL====");
    print("1. Cupos por género");
    print("2. Busqueda de peliculas por rango de precio");
    print("3. Actualizar precio de pelicula");
    print("4.Agregar pelicula");
    print("5 Eliminar pelicula");
    print("6. Salir");
    print("=======================");
#aqui se pide una opción al usuario y se usa Try-Except si ingresa una opción no valida
def leer_opc():
    try:
        opc = int(input("ingrese una opción: "));
        if(opc >= 1 and opc<= 6):
            return opc;
        else:
            raise ValueError;
    except ValueError:
        print("debe seleccionar una opción valida");
#validaciones, se eliminan espacios en blanco con .strip
def validar_codigo(codigo):
    return (codigo.strip()!= "");

def validar_titulo(titulo):
    return (titulo.strip()!= "");

def validar_genero(genero):
    return (genero.strip()!= "");

def validar_duracion_min(duracion_min):
    return (duracion_min > 0);

#se valida que la clasificacion sea A, B o C
def validar_clasificacion(clasificacion):
    return (clasificacion == "A" or clasificacion == "B" or clasificacion == "C");

def validar_idioma(idioma):
    return (idioma.strip()!= "");

#se valida que el usuario ingrese "s" o "n" y se usa lower para no distinguir minusculas
def validar_es_3d(es_3d):
    return (es_3d.lower() == "s" or es_3d.lower() == "n");

def validar_precio(precio):
    return (precio > 0);

def validar_cupos(cupos):
    return (cupos >= 0);

#funcion para calcular los cupos de un genero
def cupos_genero(genero):
    total_cupos = 0;
    #recorre todas las peliculas
    for codigo in peliculas:
        #compara el genero
        if (peliculas[codigo][1].lower() == genero.lower()):
            #suma los cupos de la pelicula encontrada
            total_cupos += cartelera [codigo][1];
    print(f"el total de los cupos disponibles es {total_cupos}");

#funcion para buscar peliculas segun el rango de precio
def busqueda_precio(p_min, p_max):
    encontrados = [];

    #recorre la cartelera
    for codigo in cartelera:
        precio = cartelera [codigo][0];
        cupos = cartelera [codigo][1];

        #revisa si el precio esta dentro del rango y si la pelicula tiene cupos disponibles
        if (precio >= p_min and precio <=p_max and cupos > 0):
            #se agrega un elemento con append
            titulo = peliculas.append(f"{titulo} : {codigo}");
    #se ordena alfabeticamente los resultados 
    encontrados.sort();
    #se usa len() para tener la cantidad de elementos que tiene la lista encontrada
    if(len(encontrados) == 0):
        print("no hay peliculas en ese rango de precios");
    else:
        print("las peliculas encontradas son: ");
        print(encontrados);

#funcion actualizar el precio de una pelicula
def actualizar_precio(codigo, nuevo_precio):
    #se usa upper para no distinguir mayusculas
    codigo = codigo.upper();

    if (codigo not in cartelera):
        return False;
    #se actualiza el precio de la pelicula
    cartelera [codigo][0] = nuevo_precio;
    return True;

#funcion para agregar pelicula nueva
def agregar_pelicula(codigo,titulo,genero,duracion_min,clasificacion,idioma,es_3d,precio,cupos):
    codigo = codigo.upper();
    if (codigo in peliculas):
        return False;

    #se crea registro en el diccionario peliculas
    peliculas[codigo] = [titulo,genero,duracion_min,clasificacion,idioma,es_3d];
     #se crea el registro en el diccionario cartelera
    cartelera[codigo] = [precio, cupos];
    return True;

#funcion para eliminar una pelicula
def eliminar_pelicula(codigo):
    codigo = codigo.upper();

    if (codigo not in peliculas):
        return False;

    #se elimina la pelicula de ambos diccionarios
    del peliculas [codigo];
    del cartelera [codigo];
    return True;

#se usa el bucle while para ejecutar el menu hasta que se escoja la opción 6
while True:
    menu();
    opc = leer_opc();

    if (opc == 1):
        genero = input("ingrese género a consultar: ");
        cupos_genero(genero);

    elif(opc == 2):
        try:
            p_min = int(input("Ingrese precio minimo: "));
            p_max = int(input("Ingrese precio maximo: "));

            if (p_min > p_max):
                print("El rango no es valido");
            else:
                busqueda_precio(p_min, p_max);
        except ValueError:
            print("Debe ingresar valores enteros");

    elif (opc == 3):
        while True:
            codigo = input("Ingrese código de la pelicula: ");
            try:
                nuevo_precio = int(input("ingrese nuevo precio"));
                if (not validar_precio(nuevo_precio)):
                    print("El precio debe ser mayor a 0");
                else:
                    resultado = actualizar_precio(codigo, nuevo_precio);
                    if (resultado):
                        print("Precio actualizado correctamente");
                    else:
                        print("El codigo no existe");
            except ValueError:
                print("Debe ingresar un número");
            continuar = input("Desea actualizar otro precio (s/n)?: ");
            if (continuar.lower() == "n"):
                break;

    elif (opc == 4):
        codigo = input("Ingrese codigo de pelicula: ");
        titulo = input("Ingrese titulo: ");
        genero = input("Ingrese género: ");
        duracion = input("Ingrese duración (minutos): ");
        clasificacion = input("Ingrese clasificación: ");
        idioma = input("Ingrese idioma: ");
        es_3d = input("¿Es 3D? (s/n): ");
        
        try:
            precio = int(input("Ingrese precio: "));
            cupos = int(input("Ingrese cupos: "));
        except ValueError:
            print("El precio y los cupos deben ser números");
        
        if (not validar_codigo(codigo)):
            print("Codigo invalido");
        elif (not validar_titulo(titulo)):
            print("Titulo invalido");
        elif (not validar_genero(genero)):
            print("Género invalido");
        elif (not validar_duracion_min(duracion)):
            print("Duración invalida");
        elif (not validar_clasificacion(clasificacion)):
            print("Clasificación invalida");
        elif (not idioma(idioma)):
            print("Idioma invalido");
        elif (validar_es_3d(es_3d)):
            print("3D invalido");
        elif (validar_precio(precio)):
            print("Precio invalido");
        elif (validar_cupos(cupos)):
            print("Cupos invalidos");
        else:
            if (es_3d.lower() == "s"):
                es_3d = True;
            else:
                es_3d = False;
            resultado = agregar_pelicula(codigo,titulo,genero,duracion,clasificacion,idioma,es_3d,precio,cupos);
            if (resultado):
                print("Pelicula agregada");
            else:
                print("el codigo no existe");
    elif (opc == 5):
        if(len(peliculas) == 0):
            print("No hay peliculas registradas");
        else:
            codigo = input("Ingrese el codigo de la pelicula");
            resultado = eliminar_pelicula(codigo);
            if (resultado):
                print("Pelicula eliminada");
            else:
                print("El codigo no existe");

    elif (opc == 6):
        print("programa finalizado");
        break;
    else:
        print("Debe ingresar una opción valida");